from flask import Flask, jsonify
from api.blueprints.user.views import user


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # reads app configuration settings from config/settings
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # in the case you want to override app default settings
    #  e.g. a test environment
    if settings_override:
        app.config.update(settings_override)

    # registers various application blueprints
    app.register_blueprint(user)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return 'Chemondis API application'

    @app.errorhandler(404)
    def resource_not_found(error):
        """

        :param error: error instance
        :return: 404 response of when a request resource is not found
        """

        response = jsonify(dict(error='Not found',
                                message='The requested URL was not'
                                        ' found on the server.'))
        response.status_code = 404
        return response

    return app
