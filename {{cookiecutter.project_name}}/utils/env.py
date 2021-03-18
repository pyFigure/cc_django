"""
.envrc 文件是 direnv 项目的配置文件
Env类优先读取 .envrc 中的配置，再读取环境变量的配置
"""
import os
import threading

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Env(metaclass=SingletonType):
    """
    单利模式
    """
    _data = dict()
    _envs = []  # 存储代码中用到的 env

    def __init__(self, file_path: str = ".envrc") -> None:
        envs_from_file = self.read_from_dot_envrc(file_path=file_path)
        self._data.update(envs_from_file)
        self._data.update(os.environ)

    @staticmethod
    def read_from_dot_envrc(file_path: str = ".envrc") -> dict:
        """从 .envrc 中读取环境环境变量"""
        envs = dict()
        # 兼容文件不存在的情况
        if os.path.exists(file_path):
            with open(file_path) as f:
                for line in f.readlines():
                    # 跳过空行，警号注释
                    if line.isspace() or line.startswith('#'):
                        continue
                    k, v = line.split()[1].split('=', 1)
                    envs[k.strip()] = v.strip().strip("'").strip('"')
        else:
            print("[warning]: envrc (%s) not exist, please check" % file_path)
        return envs

    def get(self, key: str, default: str = None) -> str:
        """
        获取环境变量值
        :param key: 环境变量 key
        :param default: 默认值
        :return: value
        """
        # 保存 env
        if key not in self._envs:
            self._envs.append(key)

        return self._data.get(key, default)

    def check_missed_env(self) -> list:
        """检测 .envrc 看是否满足系统所需，并返回未命中变量"""
        missed = []
        for env in self._envs:
            try:
                self._data[env]
            except KeyError:
                missed.append(env)
        return missed
