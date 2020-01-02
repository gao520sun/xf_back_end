sail_user_api:
	gunicorn -c python:user_api.conf.gunicorn user_api.server:proflask