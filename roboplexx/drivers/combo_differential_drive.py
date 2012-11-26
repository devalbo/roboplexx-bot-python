from roboplexx import rpx_util
from ..devices import dev_basic

__author__ = 'ajb'

@rpx_util.rpx_device
class DifferentialDrive(dev_basic.RpxDevice):

  def __init__(self, device_id, motor_left, motor_right):
    dev_basic.RpxDevice.__init__(self, device_id)
    self._motor_left = motor_left
    self._motor_right = motor_right

  @rpx_util.rpx_multi_getter("motor_speeds")
  def get_motor_speeds(self):
    return {"left_speed": self._motor_left.get_motor_speed(),
            "right_speed": self._motor_right.get_motor_speed()}

  @rpx_util.rpx_multi_setter("motor_speeds", ["left_speed", "right_speed"])
  def set_motor_speeds(self, left_speed, right_speed):
    print "SETTING MOTOR SPEEDS"
    self._motor_left.set_motor_speed(left_speed)
    self._motor_right.set_motor_speed(right_speed)
    return {"left_speed": self._motor_left.get_motor_speed(),
            "right_speed": self._motor_right.get_motor_speed()}

  def drvr_init(self):
    pass

  def drvr_un_init(self):
    pass

