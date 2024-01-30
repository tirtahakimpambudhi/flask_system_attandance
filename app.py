from flask import Flask
from config.config import Config
from blueprints.auth_bp import auth_views
from blueprints.main_bp import main_views
import logging

app = Flask(__name__)

def create_app():
    """
    Application factory function to create and configure the Flask app.
    """
    try:
        app.register_blueprint(auth_views)
        app.register_blueprint(main_views)
        app.config.from_object(Config())
    except ImportError as e:
        logging.error(f"Import error: {e}")
        raise e
    return app

@app.route("/env", methods=["GET"])
def env():
    """
    Endpoint to display the DATABASE configuration.
    """
    try:
        database_config = app.config["DATABASE"]
        return "", 200
    except KeyError as e:
        logging.error(f"Key error in config: {e}")
        return str(e), 500

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
