from roboplexx import rpx_util

__author__ = 'ajb'

@rpx_util.rpx_device
class DemoCamera(rpx_util.RpxDevice):

  def __init__(self, device_id):
    rpx_util.RpxDevice.__init__(self, device_id)

  @rpx_util.rpx_getter("demo_camera_version")
  def get_demo_camera_version(self):
    return "Demo Camera 1.2.3"

  @rpx_util.rpx_getter("latest_image")
  def get_latest_image(self):
    return ""

  @rpx_util.rpx_getter("video_stream")
  def get_video_stream(self):
    return ""

  def drvr_init(self):
    pass

  def drvr_un_init(self):
    pass

