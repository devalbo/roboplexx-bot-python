from roboplexx import settings
from roboplexx.drivers import drvr_demo_camera, drvr_demo_motor_controller, drvr_demo_multimotor_controller

__author__ = 'ajb'

from roboplexx.rpx_host import dev_host
from roboplexx.io_configs import configurations

from flask import Flask

app = Flask(__name__)

#app.register_blueprint(dev_io, url_prefix='/io')
app.register_blueprint(dev_host, url_prefix='/host')
app.register_blueprint(configurations, url_prefix='/configurations')

#class RpxGetterView(View):
#  methods = ["GET"]
#
#  def __init__(self, dev_instance, prop_get_method_name):
#    self._device_instance = dev_instance
#    self._prop_get_method_name = prop_get_method_name
#
#  def dispatch_request(self):
#    return getattr(self._device_instance, self._prop_get_method_name)()
#
#
#class RpxSetterView(View):
#  methods = ["POST"]
#
#  def __init__(self, dev_instance, prop_set_method_name):
#    self._device_instance = dev_instance
#    self._prop_set_method_name = prop_set_method_name
#
#  def dispatch_request(self):
#    value = request.form['value']
#    return getattr(self._device_instance, self._prop_set_method_name)(value)
#
#
#def _register_multi_host_device(device_instance, device_id):
#  pass
#
#def _register_device(device_instance, device_id):
#  try:
#    for rpx_prop, rpx_prop_get_method_name in device_instance.rpx_getters.iteritems():
#      getter_path = "/io/%s/%s" % (device_id, rpx_prop)
#      endpoint_name = "io.%s.prop.get.%s" % (device_id, rpx_prop)
#      app.add_url_rule(
#        getter_path,
#        view_func=RpxGetterView.as_view(endpoint_name,
#          dev_instance=device_instance, prop_get_method_name=rpx_prop_get_method_name)
#      )
#
#    for rpx_prop, rpx_prop_set_method_name in device_instance.rpx_setters.iteritems():
#      setter_path = "/io/%s/%s" % (device_id, rpx_prop)
#      endpoint_name = "io.%s.prop.set.%s" % (device_id, rpx_prop)
#      app.add_url_rule(
#        setter_path,
#        view_func=RpxSetterView.as_view(endpoint_name,
#          dev_instance=device_instance, prop_set_method_name=rpx_prop_set_method_name)
#      )
#
#    for rpx_command, rpx_command_method_name in device_instance.rpx_commands.iteritems():
#      cmd_path = "/io/%s/cmd/%s" % (device_id, rpx_command)
#      app.add_url_rule(
#        cmd_path,
#        endpoint="io.%s.cmd.%s" % (device_id, rpx_command),
#        view_func=getattr(device_instance, rpx_command_method_name),
#        methods=['GET', 'POST']
#      )
#
#  except AttributeError, e:
#    print "No RPX attributes discovered when registering device - are you sure this is an RPX device?"
#
#
#def register_device(device_instance, device_id):
#  print "Registering %s" % device_id
#
#  _register_device(device_instance, device_id)



mc_left = drvr_demo_motor_controller.DemoMotorController("mc_left")
mc_right = drvr_demo_motor_controller.DemoMotorController("mc_right")
multi_mc1 = drvr_demo_multimotor_controller.DemoMultiMotorController("multi_mc1")
multi_mc2 = drvr_demo_multimotor_controller.DemoMultiMotorController("multi_mc2")
camera1 = drvr_demo_camera.DemoCamera("camera1")
camera2 = drvr_demo_camera.DemoCamera("camera2")

multi_mc1.activate()
multi_mc2.activate()

#mc_left.register_app(app)
#mc_right.register_app(app)
multi_mc1.register_with_host(app)
multi_mc2.register_with_host(app)
camera1.register_with_host(app)
camera2.register_with_host(app)


#register_device(mc_left, "mc_left")
#register_device(mc_right, "mc_right")
#register_device(multi_mc1, "multi_mc1")
#register_device(multi_mc2, "multi_mc2")

print app.url_map
#print dir(app.url_map)
#print app.url_map['/io/mc_right/cmd/stop_motor']

# start web application
if __name__ == "__main__":
  app.run(
    debug=settings.DEBUG_MODE_ON,
    host=settings.ROBOPLEXX_HOST_NAME,
    port=settings.ROBOPLEXX_PORT)

