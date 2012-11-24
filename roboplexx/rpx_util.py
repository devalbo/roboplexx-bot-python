__author__ = 'ajb'

from flask.views import View
from flask import request

def rpx_device(cls):
  cls.rpx_getters = {}
  cls.rpx_setters = {}
  cls.rpx_commands = {}
  for method_name in dir(cls):
    method = getattr(cls, method_name)
    if hasattr(method, '_rpx_getter'):
      cls.rpx_getters.update(method._rpx_getter)
    if hasattr(method, '_rpx_setter'):
      cls.rpx_setters.update(method._rpx_setter)
    if hasattr(method, '_rpx_command'):
      cls.rpx_commands.update(method._rpx_command)

  return cls


def rpx_getter(prop_name):
  def wrapper(func):
    func._rpx_getter = {prop_name: func.__name__}
    return func
  return wrapper

def rpx_setter(prop_name):
  def wrapper(func):
    func._rpx_setter = {prop_name: func.__name__}
    return func
  return wrapper

def rpx_command(cmd_name):
  def wrapper(func):
    func._rpx_command = {cmd_name: func.__name__}
    return func
  return wrapper


class RpxPropGetterView(View):
  methods = ["GET"]

  def __init__(self, dev_instance, prop_get_method_name):
    self._device_instance = dev_instance
    self._prop_get_method_name = prop_get_method_name

  def dispatch_request(self):
    return getattr(self._device_instance, self._prop_get_method_name)()


class RpxPropSetterView(View):
  methods = ["POST"]

  def __init__(self, dev_instance, prop_set_method_name):
    self._device_instance = dev_instance
    self._prop_set_method_name = prop_set_method_name

  def dispatch_request(self):
    value = request.form['value']
    return getattr(self._device_instance, self._prop_set_method_name)(value)


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
      getter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
      endpoint_name = "io.%s.prop.get.%s" % (self.device_id, rpx_prop)
      app.add_url_rule(
        getter_path,
        view_func=RpxPropGetterView.as_view(endpoint_name,
          dev_instance=self, prop_get_method_name=rpx_prop_get_method_name)
      )

    for rpx_prop, rpx_prop_set_method_name in self.rpx_setters.iteritems():
      setter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
      endpoint_name = "io.%s.prop.set.%s" % (self.device_id, rpx_prop)
      app.add_url_rule(
        setter_path,
        view_func=RpxPropSetterView.as_view(endpoint_name,
          dev_instance=self, prop_set_method_name=rpx_prop_set_method_name)
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

class RpxDevNotInitializedError(Exception):
  pass
