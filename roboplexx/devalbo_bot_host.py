from roboplexx import settings

__author__ = 'ajb'

import roboplexx.drivers

from roboplexx.rpx_host import dev_host
from roboplexx.io_configs import configurations
from roboplexx.devalbo_bot_app import devalbo_bot_app

from flask import Flask

host = Flask(__name__)

host.register_blueprint(dev_host, url_prefix='/host')
host.register_blueprint(configurations, url_prefix='/configurations')
host.register_blueprint(devalbo_bot_app, url_prefix='/app')


mc_left = roboplexx.drivers.DemoMotorController("mc_left")
mc_right = roboplexx.drivers.DemoMotorController("mc_right")
#mc_left = roboplexx.drivers.PololuSimpleMotorController("mc_left")
#mc_right = roboplexx.drivers.PololuSimpleMotorController("mc_right")
diff_drive = roboplexx.drivers.DifferentialDrive("diff_drive", mc_left, mc_right)
camera = roboplexx.drivers.DemoCamera("camera")

mc_left.activate()
mc_right.activate()
diff_drive.activate()
camera.activate()

mc_left.register_with_host(host)
mc_right.register_with_host(host)
diff_drive.register_with_host(host)
camera.register_with_host(host)

print host.url_map


# start web application
if __name__ == "__main__":
  host.run(
    debug=settings.DEBUG_MODE_ON,
    host=settings.ROBOPLEXX_HOST_NAME,
    port=settings.ROBOPLEXX_PORT)
