from roboplexx import rpx_util

__author__ = 'ajb'

from .. import devices

@rpx_util.rpx_device
class DemoMotorController(devices.McBasic):

  def __init__(self, device_id):
    devices.McBasic.__init__(self, device_id)
    self._motor_speed = "0"

  @rpx_util.rpx_getter("demo_motor_version")
  def get_demo_motor_version(self):
    return "Demo Motor 1.2.3"

  def drvr_init(self):
    pass

  def drvr_un_init(self):
    pass

  def drvr_set_motor_speed(self, speed):
    self._motor_speed = speed
    return self._motor_speed

  def drvr_get_motor_speed(self):
    return self._motor_speed
