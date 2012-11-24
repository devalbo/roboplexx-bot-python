from roboplexx import rpx_util

__author__ = 'ajb'

import unittest

@rpx_util.rpx_device
class SampleRpxDevice(rpx_util.RpxDevice):

  def __init__(self):
    self._p1 = ""
    self._p2 = ""

  @rpx_util.rpx_setter("p1")
  def set_property1(self, value):
    self._p1 = value
    print "Setting p1 to %s" % value

  @rpx_util.rpx_setter("p2")
  def set_property2(self, value):
    self._p2 = value
    print "Setting p2 to %s" % value

  @rpx_util.rpx_getter("p1")
  def get_property1(self):
    print "Getting p1 value"
    return self._p1

  @rpx_util.rpx_command("cmd1")
  def cmd_cmd1(self):
    print "Sending cmd1"


class TestRpxDevice(unittest.TestCase):

  def test_rpx_decorators(self):
    dev = SampleRpxDevice()
    self.assertEqual(1, len(dev.rpx_getters))
    self.assertEqual(2, len(dev.rpx_setters))
    self.assertEqual(3, len(dev.rpx_commands))

  def test_applying_rpx_values(self):
    dev = SampleRpxDevice()
    rpx_prop = "p1"
    rpx_prop_value = "abc"
    getattr(dev, dev.rpx_setters[rpx_prop])(rpx_prop_value)
    self.assertEqual(rpx_prop_value, getattr(dev, dev.rpx_getters[rpx_prop])())
