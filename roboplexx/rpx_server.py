from roboplexx import settings

__author__ = 'ajb'

from rpx_io import dev_io
from roboplexx.rpx_host import dev_host
from roboplexx.io_configs import configurations

from flask import Flask
app = Flask(__name__)

app.register_blueprint(dev_io, url_prefix='/io')
app.register_blueprint(dev_host, url_prefix='/host')
app.register_blueprint(configurations, url_prefix='/configurations')


@app.route("/")
def hello():
  return "Hello World!"

# start web application
if __name__ == "__main__":
  app.run(
    debug=settings.DEBUG_MODE_ON,
    host=settings.ROBOPLEXX_HOST_NAME,
    port=settings.ROBOPLEXX_PORT)
