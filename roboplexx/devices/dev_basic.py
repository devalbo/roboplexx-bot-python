__author__ = 'ajb'

from ..rpx_util import *

@rpx_device
class RpxDevice(object):

  def __init__(self, device_id):
    self.device_id = device_id

  @rpx_command("rpx_activate")
  def activate(self):
    return self.drvr_init()

  @rpx_command("rpx_deactivate")
  def deactivate(self):
    return self.drvr_uninit()

  def drvr_init(self):
    raise NotImplementedError("%s not implemented for device ID '%s'" %
                              (self.drvr_init.__name__, self.device_id))

  def drvr_un_init(self):
    raise NotImplementedError("%s not implemented for device ID '%s'" %
                              (self.drvr_uninit.__name__, self.device_id))

  def register_with_host(self, app):
    for rpx_prop, rpx_prop_get_method_name in self.rpx_getters.iteritems():
      setter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
      endpoint_name = "io.%s.prop.get.%s" % (self.device_id, rpx_prop)
      app.add_url_rule(
        setter_path,
        view_func=RpxPropGetterView.as_view(endpoint_name,
          dev_instance=self,
          prop_get_method_name=rpx_prop_get_method_name,
          prop_set_url=setter_path,
          prop_label=rpx_prop
        )
      )

    for rpx_prop, rpx_prop_set_method_name in self.rpx_setters.iteritems():
      setter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
      endpoint_name = "io.%s.prop.set.%s" % (self.device_id, rpx_prop)
      app.add_url_rule(
        setter_path,
        view_func=RpxPropSetterView.as_view(endpoint_name,
          dev_instance=self,
          prop_set_method_name=rpx_prop_set_method_name)
      )

    for rpx_command, rpx_command_method_name in self.rpx_commands.iteritems():
      cmd_path = "/io/%s/cmd/%s" % (self.device_id, rpx_command)
      endpoint_name = "io.%s.cmd.%s" % (self.device_id, rpx_command)
      app.add_url_rule(
        cmd_path,
        endpoint=endpoint_name,
        view_func=getattr(self, rpx_command_method_name),
        methods=['GET', 'POST']
      )

    for rpx_multi_prop, rpx_multi_prop_getter in self.rpx_multi_getters.iteritems():
      getter_path = "/io/%s/%s" % (self.device_id, rpx_multi_prop)
      endpoint_name = "io.%s.multiprop.get.%s" % (self.device_id, rpx_multi_prop)
      app.add_url_rule(
        getter_path,
        view_func=RpxMultiPropGetterView.as_view(endpoint_name,
          dev_instance=self,
          prop_get_method_name=rpx_multi_prop_getter,
          prop_set_url=getter_path
        )
      )

    for rpx_multi_prop, rpx_multi_prop_setter in self.rpx_multi_setters.iteritems():
      setter_path = "/io/%s/%s" % (self.device_id, rpx_multi_prop)
      endpoint_name = "io.%s.multiprop.set.%s" % (self.device_id, rpx_multi_prop)
      app.add_url_rule(
        setter_path,
        view_func=RpxMultiPropSetterView.as_view(endpoint_name,
          dev_instance=self,
          prop_set_method_name=rpx_multi_prop_setter.func_name,
          multi_names=rpx_multi_prop_setter.multi_names,
          prop_set_url=setter_path
        )
      )