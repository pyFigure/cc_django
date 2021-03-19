import os
import shutil


class GenericCCHooks(object):
    """
    通用 CookieCutter Hooks
    file_path_list: 定义待删除的文件路径
    dir_path_list: 定义待删除的文件夹路径
    """

    file_path_list = []
    dir_path_list = []

    def __init__(self, removable):
        self.removable = removable

    def remove(self):
        if self.removable.lower() == 'n':
            for dir_path in self.dir_path_list:
                if os.path.exists(dir_path):
                    shutil.rmtree(dir_path)

            for file_name in self.file_path_list:
                if os.path.exists(file_name):
                    os.remove(file_name)


class CeleryCCH(GenericCCHooks):
    file_path_list = [
        "{{cookiecutter.project_name}}/celery.py",
        "config/common/celery.py",
    ]


class MDEditorCCH(GenericCCHooks):
    file_path_list = [
        'config/common/mdeditor.py'
    ]


class S2iCCH(GenericCCHooks):
    file_path_list = ['app.sh']
    dir_path_list = ['.s2i']


class SwaggerCCH(GenericCCHooks):
    file_path_list = [
        "{{cookiecutter.project_name}}/swagger.py",
        'config/common/swagger.py'
    ]


class SphinxCCH(GenericCCHooks):
    dir_path_list = ['docs']


class TaggitCCH(GenericCCHooks):
    dir_path_list = ['utils/taggit']


class DemoCCH(GenericCCHooks):
    dir_path_list = ['demo']
    file_path_list = ['utils/drf/validators.py']


if __name__ == "__main__":
    cch_classes = [
        CeleryCCH('{{cookiecutter.use_celery}}'),
        MDEditorCCH('{{cookiecutter.use_mdeditor}}'),
        S2iCCH('{{cookiecutter.use_s2i}}'),
        SwaggerCCH('{{cookiecutter.use_swagger}}'),
        SphinxCCH('{{cookiecutter.use_sphinx}}'),
        TaggitCCH('{{cookiecutter.use_taggit}}'),
        DemoCCH('{{cookiecutter.use_demo}}')
    ]

    for cch in cch_classes:
        cch.remove()
