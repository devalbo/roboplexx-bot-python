__author__ = 'ajb'

import unittest
import requests

DIFF_DRIVE_ROOT = "http://127.0.0.1:5000/io/diff_drive/"

class TestDifferentialDrive(unittest.TestCase):

  def test_get_motor_speeds(self):
    print "Get motor speeds test"
    r = requests.get(DIFF_DRIVE_ROOT + "motor_speeds")
    print "%s >> %s" % (DIFF_DRIVE_ROOT + "motor_speeds", r.text)
    print

#  def test_set_motor_speeds(self):
#    print "Set motor speeds test"
#    for mc_left_speed, mc_right_speed in [("29", "55"), ("33", "44")]:
#      mc_left_payload = {'value': mc_left_speed}
#      r = requests.post(self._getMcLeftPropUrl("motor_speed"), data=mc_left_payload)
#      print "%s >> %s" % (self._getMcLeftPropUrl("motor_speed"), r.text)
#
#      mc_right_payload = {'value': mc_right_speed}
#      r = requests.post(self._getMcRightPropUrl("motor_speed"), data=mc_right_payload)
#      print "%s >> %s" % (self._getMcRightPropUrl("motor_speed"), r.text)
#    print
#
#  def test_get_firmware_version(self):
#    print "Get demo motor version test"
#    r = requests.get(self._getMcLeftPropUrl("demo_motor_version"))
#    print "%s >> %s" % (self._getMcLeftPropUrl("demo_motor_version"), r.text)
