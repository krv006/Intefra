mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

flush:
	python3 manage.py flush --no-input

migdel:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

pip:
	pip freeze > requirements.txt


celery:
	celery -A root worker -l INFO