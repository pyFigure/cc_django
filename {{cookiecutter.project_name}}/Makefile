env="dev"

freeze:
	pip freeze > requirements.txt
superuser:
	python manage.py createsuperuser
make:
	python manage.py makemigrations account
	{%- if cookiecutter.use_demo.lower() == 'y' %}
	python manage.py makemigrations demo
	{%- endif %}
	python manage.py migrate
check_env:
	python manage.py check_env
push:
	python utils/env.py push
pull:
	python utils/env.py pull
flush:
	python utils/env.py flush
use:
	python utils/env.py use --params $(env)
clean:
	rm -rf db.sqlite3
	rm -rf account/migrations
	{%- if cookiecutter.use_demo.lower() == 'y' %}
	rm -rf demo/migrations
	{%- endif %}
