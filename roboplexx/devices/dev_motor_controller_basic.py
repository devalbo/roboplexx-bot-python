from roboplexx import rpx_util

__author__ = 'ajb'

@rpx_util.rpx_device
class McBasic(rpx_util.RpxDevice):

  def __init__(self, device_id):
    rpx_util.RpxDevice.__init__(self, device_id)
    self._direction_flipped = False

  @rpx_util.rpx_getter("direction_flipped")
  def direction_flipped(self):
    return self._direction_flipped

  @rpx_util.rpx_setter("direction_flipped")
  def set_direction_flipped(self, flipped):
    self._direction_flipped = flipped
    return self._direction_flipped

  @rpx_util.rpx_getter("motor_speed")
  def get_motor_speed(self):
    return self.drvr_get_motor_speed()

  @rpx_util.rpx_setter("motor_speed")
  def set_motor_speed(self, speed):
    print "SETTING MOTOR SPEED TO " + speed
    speed_set = self.drvr_set_motor_speed(speed)
    self._motor_speed = speed_set
    return self._motor_speed

  @rpx_util.rpx_command("stop_motor")
  def cmd_stop_motor(self):
    return "STOP COMMAND FOR %s" % self.device_id

  def drvr_get_motor_speed(self):
    raise NotImplementedError("%s not implemented for device ID '%s'" %
                              (self.drvr_get_motor_speed.__name__, self.device_id))

  def drvr_set_motor_speed(self, speed):
    raise NotImplementedError("%s not implemented for device ID '%s'" %
                              (self.drvr_set_motor_speed.__name__, self.device_id))

  def drvr_cmd_stop_motor(self):
    raise NotImplementedError("%s not implemented for device ID '%s'" %
                              (self.drvr_cmd_stop_motor.__name__, self.device_id))

