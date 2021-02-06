![image](https://github.com/pyfs/cc_django/blob/master/images/installing-1.png)
![image](https://github.com/pyfs/cc_django/blob/master/images/installing-2.png)

## 生成 Django 项目的 Cookiecutter 模板

# 项目支持

1. 环境支持: 开发环境，测试环境，生产环境
2. Django 项目最佳实践
3. 自定义用户模型支持
4. 环境变量管理: 从文件和系统环境变量中读取
5. 生产环境配置支持 (uwsgi)
6. 支持 pyenv 自动创建 virtualenv
7. 按需加载常见依赖包及相关配置(grappelli, taggit, mdeditor)等
8. source2image 启动脚本(支持 uwsgi, celery worker, beat, flower 独立运行)
9. 自定义 python 版本支持(默认 3.7.5)

# 安装 cookiecutter 

MacOS 推荐使用 Home brew 安装，更多方法参考[官方部署文档](https://cookiecutter.readthedocs.io/en/1.7.0/installation.html)

```shell script
brew install cookiecutter
```

# 安装 pyenv 

自动创建 python 虚拟环境依赖 pyenv，需在使用前安装 pyenv 和 pyenv-virtualenv

```shell script
# pyenv 支持脚本一键安装
$ curl https://pyenv.run | bash

# pyenv-virtualenv 安装
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

官方文档: [pyenv](https://github.com/pyenv/pyenv)
Pyenv插件: [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

# 快速使用

```shell script

cookiecutter https://github.com/pyFigure/cc_django

```

# 教程: 手把手教你打造 Django 项目模板

[1. django 项目结构优化](https://github.com/pyfs/cc_django/blob/master/docs/1.%20django%20%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84%E4%BC%98%E5%8C%96.md)

[2. 解决环境变量加载问题](https://github.com/pyfs/cc_django/blob/master/docs/2.%20%E8%A7%A3%E5%86%B3%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E5%8A%A0%E8%BD%BD%E9%97%AE%E9%A2%98.md)

[3. 添加常用开发依赖包](https://github.com/pyfs/cc_django/blob/master/docs/3.%20%E6%B7%BB%E5%8A%A0%E5%B8%B8%E7%94%A8%E5%BC%80%E5%8F%91%E4%BE%9D%E8%B5%96%E5%8C%85.md)

[4. cookiecutter功能介绍](https://github.com/pyfs/cc_django/blob/master/docs/4.%20cookiecutter%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D.md)

[5. 删除jinja2多余的空行](https://github.com/pyfs/cc_django/blob/master/docs/5.%20%E5%88%A0%E9%99%A4jinja2%E5%A4%9A%E4%BD%99%E7%9A%84%E7%A9%BA%E8%A1%8C.md)

[6. pre_gen_project按需加载项目依赖](https://github.com/pyfs/cc_django/blob/master/docs/6.%20pre_gen_project%E6%8C%89%E9%9C%80%E5%8A%A0%E8%BD%BD%E9%A1%B9%E7%9B%AE%E4%BE%9D%E8%B5%96.md)

[7. post_gen_project按需删除项目文件](https://github.com/pyfs/cc_django/blob/master/docs/7.%20post_gen_project%E6%8C%89%E9%9C%80%E5%88%A0%E9%99%A4%E9%A1%B9%E7%9B%AE%E6%96%87%E4%BB%B6.md)

[8. 总结](https://github.com/pyfs/cc_django/blob/master/docs/8.%20%E6%80%BB%E7%BB%93.md)


> ### 5. TODO

1. 拆分 requirements.txt
2. oauth2 支持

---
![image](https://github.com/pyfs/cc_django/blob/master/docs/images/%E5%85%A5%E7%BE%A4%E5%85%AC%E5%91%8A.png)
