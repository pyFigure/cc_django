clean:
	rm -rf db.sqlite3
	rm -rf account/migrations
	{%- if cookiecutter.use_demo.lower() == 'y' %}
	rm -rf demo/migrations
	{%- endif %}
install:
	pip freeze > requirements.txt
	python manage.py makemigrations
	python manage.py migrate
