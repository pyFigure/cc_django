"""
                _ _
               | (_)
   ___ ___   __| |_  __ _ _ __   __ _  ___
  / __/ __| / _` | |/ _` | '_ \ / _` |/ _ \\
 | (_| (__ | (_| | | (_| | | | | (_| | (_) |
  \___\___| \__,_| |\__,_|_| |_|\__, |\___/
        ______  _/ |             __/ |
       |______||__/             |___/
"""
import re
import subprocess
import sys


class ColorSchema(object):
    """
    基于 shell 的配色方案
    """
    TERMINATOR = "\033[0m"  # 统一终止符

    FONT_RED = "\033[31m"
    FONT_GREEN = "\033[32m"
    FONT_YELLOW = "\033[33m"
    FONT_BLUE = "\033[34m"
    FONT_VIOLET = "\033[35m"
    FONT_SKY_BLUE = "\033[36m"

    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_VIOLET = "\033[45m"
    BG_SKY_BLUE = "\033[46m"

    def end(self, message):
        print(self.BG_VIOLET + message + self.TERMINATOR)

    def info(self, message):
        message = "[Info] " + message
        print(self.FONT_SKY_BLUE + message + self.TERMINATOR)

    def warning(self, message):
        message = "[🔔️] " + message
        print(self.FONT_YELLOW + message + self.TERMINATOR)

    def error(self, message):
        message = "[🆘] " + message
        print(self.FONT_RED + message + self.TERMINATOR)

    def success(self, message):
        message = "[✅] " + message
        print(self.FONT_GREEN + message + self.TERMINATOR)

    def title(self, message):
        message = "[🚀] " + message
        print(self.BG_GREEN + message + self.TERMINATOR)


class MessageBlock(ColorSchema):
    """
    屏幕输出的信息块，封装统一样式
    """
    TITLE = None
    START = None
    END = None

    def __init__(self):
        if self.TITLE:
            self.title(message=self.TITLE)
        if self.START:
            self.info(message=self.START)
        self.action()
        if self.END:
            self.end(message=self.END)

    def action(self):
        pass

    @staticmethod
    def decode_output(output):
        """
        decode check_output from byte to utf-8
        @param output: subprocess check_output result
        """
        return output.decode('utf-8').strip().strip('\n')


class Welcome(MessageBlock):
    TITLE = "Hi Man, Glad to see you here, Welcome to Star!"
    START = ">>> https://github.com/pyfs/cc_django.git <<<"
    END = "----------------------------------------------------------"

    def action(self):
        print(__doc__)


class WellDone(MessageBlock):
    END = "Congratulations, Well Done Once Again ⛽️⛽️⛽️ \nlast operation execute: make install."


class CheckProjectName(MessageBlock):
    TITLE = "检测项目名称是否合规"

    def action(self):
        reg = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
        project_name = '{{ cookiecutter.project_name }}'
        if not re.match(reg, project_name):
            self.error(' The project name(%s) invalid, use _ instead of -' % project_name)
            sys.exit(1)


class CheckPyenvInstalled(MessageBlock):
    TITLE = "检测 pyenv 是否安装"

    def action(self):
        cmd = "pyenv --version"
        if subprocess.check_call(cmd, shell=True):
            self.error("pyenv seems not installed!")
            sys.exit(1)


class CheckPythonVersion(MessageBlock):
    TITLE = "检测 python 版本 {{cookiecutter.python_version}} 是否安装"

    def action(self):
        cmd = "pyenv versions | grep -v '{{cookiecutter.python_version}}/' | grep '{{cookiecutter.python_version}}'"
        py = subprocess.check_output(cmd, shell=True)
        if self.decode_output(py) != "{{cookiecutter.python_version}}":
            self.error("python==={{cookiecutter.python_version}} not installed")
            sys.exit(1)
        self.info(self.decode_output(py))


class PyenvCreateVirtualenv(MessageBlock):
    TITLE = "用项目名创建虚拟环境"

    # 创建虚拟环境命令
    VENV_CREATE_CMD = [
        'pyenv virtualenv {{cookiecutter.python_version}} {{cookiecutter.project_name}}',
        'pyenv local {{cookiecutter.project_name}}',
    ]

    def action(self):
        cmd = 'pyenv versions --skip-aliases'
        versions = subprocess.check_output(cmd, shell=True)
        version_map = map(lambda x: x.strip(), versions.decode('utf-8').split('\n'))
        if "{{cookiecutter.python_version}}/envs/{{cookiecutter.project_name}}" not in version_map:
            self.warning("虚拟环境 {{cookiecutter.project_name}} 未曾创建，现在创建 ...")
            self.create_venv()

    def create_venv(self):
        for line in self.VENV_CREATE_CMD:
            self.success('[!] %s' % line)
            subprocess.check_call(line, shell=True)


class PipInstallRequirements(MessageBlock):
    TITLE = "安装项目 python 依赖包"
    REQUIREMENTS = {
        'default': {
            'input': 'Y',
            'pkg': [
                'Django=={{cookiecutter.django_version}}',
                'wrapt',
                'Pillow',
                'django-model-utils',
                'psycopg2-binary',
                'uWSGI',
                'django-filter',
                'django-extensions',
                'drf-extensions',
                'djangorestframework',
                'djangorestframework-jwt',
                'django-grappelli',
                'django-filebrowser',
                'feedparser'
            ],
        },
        'celery': {
            'input': '{{cookiecutter.use_celery}}',
            'pkg': [
                'django-celery-beat',
                'celery',
                'amqp',
            ],
        },
        'mdeditor': {
            'input': '{{cookiecutter.use_mdeditor}}',
            'pkg': [
                'django-mdeditor'
            ],
        },
        'taggit': {
            'input': '{{cookiecutter.use_taggit}}',
            'pkg': [
                'django-taggit',
                'django-taggit-serializer'
            ]
        },
        'swagger': {
            'input': '{{cookiecutter.use_swagger}}',
            'pkg': [
                'drf-yasg2'
            ]
        },
        'sphinx': {
            'input': '{{cookiecutter.use_sphinx}}',
            'pkg': [
                'Sphinx',
                'sphinx-autobuild',
                'sphinx-rtd-theme'
            ]
        },
        'demo': {
            'input': '{{cookiecutter.use_demo}}',
            'pkg': [
                'jsonschema',
            ]
        }
    }

    def action(self):
        requirements = []
        for key, item in self.REQUIREMENTS.items():
            if item['input'].strip().lower() == 'y':
                requirements += item['pkg']
        self.warning('[!] installing ...')
        cmd = ['pip', 'install'] + requirements
        subprocess.check_call(cmd)


class PipFreezeRequirements(MessageBlock):
    TITLE = "更新项目依赖到 requirements.txt 文件"

    def action(self):
        """
        自动更新项目依赖文件
        """
        self.warning('[!] freezing requirements ...')
        cmd = 'pip freeze'
        result = subprocess.run(cmd, shell=True, capture_output=True)
        if result.returncode:
            self.warning(result.stderr.decode('utf-8'))
        with open('./requirements.txt', 'w+') as f:
            f.write(result.stdout.decode('utf-8'))


class PreGenProjectHooks(object):
    PIPELINE = [
        'Welcome',
        'CheckProjectName',
        'CheckPyenvInstalled',
        'CheckPythonVersion',
        'PyenvCreateVirtualenv',
        'PipInstallRequirements',
        'PipFreezeRequirements',
        'WellDone',
    ]

    def __call__(self):
        for cls_name in self.PIPELINE:
            try:
                eval(cls_name)()
            except KeyError:
                print("PreGenProjectHooks has got no Attribute: %s" % cls_name)


if __name__ == '__main__':
    PreGenProjectHooks()()
