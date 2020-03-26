import logging


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format='%(filename)s:%(lineno)d in %(funcName)s(): %(message)s')

    @classmethod
    def debug(cls):
        cls()
        logger = logging.getLogger()
        return logger.debug


class A:

    def __init__(self):
        self.debug = Logger.debug()
        self.b()

    def b(self):
        self.debug('ssssssssss')

if __name__ == '__main__':
    a = A()

# Use logger for QML
# qmlRegisterType<Logger>("logger", 1, 0, "Logger");
# 
# import logger 1.0
# Logger {
#     id: logger
# }
# logger.debug("...")