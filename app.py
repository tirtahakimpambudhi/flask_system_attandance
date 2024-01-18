from flask import Flask
from config.config import Config
from blueprints.auth_bp import auth_views
from blueprints.main_bp import main_views
from logger import app_log

app = Flask(__name__)

def create_app():
    """
    Application factory function to create and configure the Flask app.
    """
    try:
        app.register_blueprint(auth_views)
        app.register_blueprint(main_views)
        app.logger = app_log.AppLogging().init_app(app)
        app.config.from_object(Config())
    except ImportError as e:
        app.logger.error(f"Import error: {e}")
        raise e
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
