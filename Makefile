.PHONY: deploy

SECRET_KEY := $(shell python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

deploy:
	heroku config:set SECRET_KEY="$(SECRET_KEY)"
	git push heroku master
