import os
import logging

class AppLogging:

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        FORMAT = '%(asctime)s [%(levelname)-5.5s] [%(funcName)10s()] %(message)s'
        logFormatter = logging.Formatter(FORMAT)
        app.logger = logging.getLogger()
        app.logger.setLevel(logging.DEBUG)

        try:
            # Membuat direktori 'log' jika tidak ada
            os.makedirs('log', exist_ok=True)

            fileHandler = logging.FileHandler('log/app.log')
            fileHandler.setFormatter(logFormatter)
            app.logger.addHandler(fileHandler)

        except Exception as e:
            # Tangani kesalahan jika gagal membuat direktori atau file log
            print(f"Error creating log directory or file: {e}")

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        app.logger.addHandler(consoleHandler)

        return app.logger
