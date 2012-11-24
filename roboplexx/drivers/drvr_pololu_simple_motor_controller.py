from roboplexx import rpx_util

__author__ = 'ajb'

from .. import devices

@rpx_util.rpx_device
class PololuSimpleMotorController(devices.McBasic):

  def __init__(self):
    self._motor_speed = 0;

  @rpx_util.rpx_getter("firmware_version")
  def get_firmware_version(self):
    return "FMV 1.2.3"

  def init(self):
    pass

  def drvr_set_motor_speed(self, speed):
    self._motor_speed = speed
    return self._motor_speed

  def drvr_get_motor_speed(self):
    return self._motor_speed



#"GO"	Exit Safe-Start
#"F"	Motor Forward
#"R"	Motor Reverse
#"B"	Motor Brake
#"D"	Get Variable
#"L"	Set Motor Limit
#"V"	Get Firmware Version
#"X"	Stop Motor