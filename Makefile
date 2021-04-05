.PHONY: deploy

deploy:
	$(shell python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' > secret_key)
	heroku config:set SECRET_KEY="$(shell cat secret_key)"
	rm secret_key
	git push heroku master
