from roboplexx import rpx_util

__author__ = 'ajb'

@rpx_util.rpx_device
class DifferentialDrive(rpx_util.RpxDevice):

  def __init__(self, device_id, motor_left, motor_right):
    rpx_util.RpxDevice.__init__(self, device_id)
    self._motor_left = motor_left
    self._motor_right = motor_right

  @rpx_util.rpx_getter("motor_speeds")
  def get_motor_speeds(self):
    return str((self._motor_left.get_motor_speed(), self._motor_right.get_motor_speed()))

  @rpx_util.rpx_setter("motor_speeds")
  def set_motor_speeds(self, motor_left_speed, motor_right_speed):
    print "SETTING MOTOR SPEEDS"
    self._motor_left.set_motor_speed(motor_left_speed)
    self._motor_right.set_motor_speed(motor_right_speed)
    return str((self._motor_left.get_motor_speed(), self._motor_right.get_motor_speed()))

  def drvr_init(self):
    pass

  def drvr_un_init(self):
    pass

