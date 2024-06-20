from flask import Flask
from config.config import Config
# from blueprints.auth_bp import auth_views
from blueprints.main_bp import main_views
from blueprints.absence_bp import absence_route
from blueprints.students_bp import students_route
from logger import app_log

app = Flask(__name__)

def create_app():
    """
    Application factory function to create and configure the Flask app.
    """
    try:
        app.register_blueprint(students_route,url_prefix='/students')
        app.register_blueprint(absence_route,url_prefix='/absence')
        app.register_blueprint(main_views)
        app.logger = app_log.AppLogging().init_app(app)
        app.config.from_object(Config())
    except ImportError as e:
        app.logger.error(f"Import error: {e}")
        raise e
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=Config().APP["host"],port=Config().APP["port"],debug=Config().APP["debug"])
