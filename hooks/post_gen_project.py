import os
import shutil


class GenericCCHooks(object):
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
        os.path.join("{{cookiecutter.project_name}}", "celery.py"),
        os.path.join("config/common/", "celery.py"),
    ]


class MDEditorCCH(GenericCCHooks):
    file_path_list = [os.path.join('config/common/', 'mdeditor.py')]


class S2iCCH(GenericCCHooks):
    file_path_list = ['app.sh']
    dir_path_list = ['.s2i']


class DemoCCH(GenericCCHooks):
    dir_path_list = ['demo']


if __name__ == "__main__":
    cch_classes = [
        CeleryCCH('{{cookiecutter.use_celery}}'),
        MDEditorCCH('{{cookiecutter.use_mdeditor}}'),
        S2iCCH('{{cookiecutter.use_s2i}}'),
        DemoCCH('{{cookiecutter.use_demo}}')
    ]

    for cch in cch_classes:
        cch.remove()
