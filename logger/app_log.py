import logging

class AppLogging:

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        FORMAT = '%(asctime)s [%(levelname)-5.5s] [%(funcName)30s()] %(message)s'
        logFormatter = logging.Formatter(FORMAT)
        app.logger = logging.getLogger()
        app.logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler('log/app.log')
        fileHandler.setFormatter(logFormatter)
        app.logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        app.logger.addHandler(consoleHandler)

        return app.logger