# @author: peizhenfei

test:
	cookiecutter .

clean:
	rm -rf new_django_project
	pyenv uninstall new_django_project
