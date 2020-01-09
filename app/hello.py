from flask import Flask
import logging
app = Flask(__name__)


@app.route('/')
def hello():
    app.logger.debug('this is debug message')
    app.logger.error('this is error message')
    app.logger.info('this is info message')
    return 'hello,world'


if __name__ == '__main__':
    app.run()

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
