clean:
	rm -rf db.sqlite3
	rm -rf account/migrations
	{%- if cookiecutter.use_demo.lower() == 'y' %}
	rm -rf demo/migrations
	{%- endif %}
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
