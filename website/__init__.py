from flask import Flask, Blueprint


def create_app():
	app = Flask(__name__)

	from .views import views
	app.register_blueprint(views)

	return app 