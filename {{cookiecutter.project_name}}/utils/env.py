"""
.envrc 文件是 direnv 项目的配置文件
Env类优先读取 .envrc 中的配置，再读取环境变量的配置
"""
import argparse
import json
import os
import threading
from configparser import ConfigParser

import redis
import wrapt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@wrapt.decorator
def check_env_sync(wrapped, instance, args, kwargs):
    if instance.sync:
        return wrapped(*args, **kwargs)
    print("[x] It seems no ENV_SYNC set, pls SET in OS  Environment")
    return None


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class MyParser(ConfigParser):

    def as_dict(self):
        """ini to dict"""
        data = dict(self._sections)
        for key, value in data.items():
            data[key] = dict(value)
        return data


class Env(metaclass=SingletonType):
    data = dict()  # 保存所有变量
    envs = []  # 存储代码中用到的 env
    parser = MyParser(comment_prefixes=['#'], allow_no_value=True)
    sync = os.environ.get("ENV_SYNC", None)
    project = "{{cookiecutter.project_name}}"

    def __init__(self, file_path: str = ".envrc") -> None:
        self.file_path = file_path
        try:
            self.envs_from_file = self.read_from_dot_envrc()
            self.data.update(self.envs_from_file)
        except Exception as e:
            print(e)
        self.data.update(os.environ)

    def read_from_dot_envrc(self) -> dict:
        envs = dict()
        self.parser.read(self.file_path, encoding='utf-8')
        for section in self.parser.sections():
            for k, v in self.parser.items(section=section):
                key = k.split()[1].upper()
                envs[key] = v
        return envs

    @staticmethod
    def _env_translate(section):
        """通过 env 字段映射转换"""
        mappings = {
            'dev': 'DEVELOP',
            'pro': 'PRODUCT'
        }
        try:
            return mappings[section]
        except KeyError:
            return "DEVELOP"

    def use(self, section):
        """使用环境变量"""
        self.uncomment()
        self.parser.read(self.file_path)
        for sec in self.parser.sections():
            if sec != self._env_translate(section=section):
                self.comment(section=sec)
        self.parser.write(open(self.file_path, 'w'), space_around_delimiters=False)

    def comment(self, section):
        """注释某个 section"""
        for k, v in self.parser.items(section=section):
            if not k.startswith("#"):
                self.parser.remove_option(section=section, option=k)
                comment = "# %s=%s" % (k, v)
                self.parser.set(section, comment)

    def uncomment(self):
        """反注释全部 items"""
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        with open(self.file_path, 'w') as f:
            new_lines = [line.strip("# ").strip("#").strip(" ") for line in lines]
            f.writelines(new_lines)

    @check_env_sync
    def push(self):
        """push envrc to redis cache"""
        self.parser.read(self.file_path)
        rc = redis.Redis.from_url(url=self.sync)
        rc.set(name=self.project, value=json.dumps(self.parser.as_dict()))

    @check_env_sync
    def pull(self):
        """pull envrc from redis cache"""
        rc = redis.Redis.from_url(url=self.sync)
        data = rc.get(name=self.project)
        if data:
            self.parser.read_dict(json.loads(rc.get(name=self.project)))
            self.parser.write(open(self.file_path, 'w'), space_around_delimiters=False)

    @check_env_sync
    def flush(self):
        """flush redis cache"""
        rc = redis.Redis.from_url(url=self.sync)
        keys = rc.keys(pattern=self.project)
        if keys:
            rc.delete(*keys)

    def get(self, key: str, default: str = None) -> str:
        """
        获取环境变量值
        :param key: 环境变量 key
        :param default: 默认值
        :return: value
        """
        if key not in self.envs:
            self.envs.append(key)
        return self.data.get(key, default)

    def check_env(self) -> list:
        """检测 .envrc 看是否满足系统所需，并返回未命中变量"""
        return list(set(self.envs) ^ set(self.data.keys()))


if __name__ == "__main__":
    # 命令行解析
    parser = argparse.ArgumentParser(description="desc")
    parser.add_argument("cmd", type=str, help='执行命令')
    parser.add_argument("--params", type=str, nargs="+", help='命令参数')
    cmd_args = parser.parse_args()

    # 执行命令
    e = Env()
    try:
        attr = getattr(e, cmd_args.cmd)
        params = cmd_args.params or []
        attr(*params)
    except Exception as e:
        print(e)
