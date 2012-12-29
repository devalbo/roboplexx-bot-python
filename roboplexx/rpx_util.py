__author__ = 'ajb'

from flask.views import View
from flask import request, render_template

def rpx_device(cls):
  cls.rpx_getters = {}
  cls.rpx_setters = {}
  cls.rpx_commands = {}
  cls.rpx_multi_getters = {}
  cls.rpx_multi_setters = {}

  for method_name in dir(cls):
    method = getattr(cls, method_name)
    if hasattr(method, '_rpx_getter'):
      cls.rpx_getters.update(method._rpx_getter)
    if hasattr(method, '_rpx_setter'):
      cls.rpx_setters.update(method._rpx_setter)
    if hasattr(method, '_rpx_command'):
      cls.rpx_commands.update(method._rpx_command)
    if hasattr(method, '_rpx_multi_getter'):
      cls.rpx_multi_getters.update(method._rpx_multi_getter)
    if hasattr(method, '_rpx_multi_setter'):
      cls.rpx_multi_setters.update(method._rpx_multi_setter)

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


class RpxMultiFieldProp:
  pass


def rpx_multi_getter(prop_name):
  def wrapper(func):
    func._rpx_multi_getter = {prop_name: func.__name__}
    return func
  return wrapper

def rpx_multi_setter(prop_name, multi_names):
  def wrapper(func):
    multi_setter = RpxMultiFieldProp()
    multi_setter.multi_names = multi_names
    multi_setter.func_name = func.__name__
    func._rpx_multi_setter = {prop_name: multi_setter}
    return func
  return wrapper


class RpxPropGetterView(View):
  methods = ["GET"]

  def __init__(self, dev_instance, prop_get_method_name, prop_set_url, prop_label):
    self._device_instance = dev_instance
    self._prop_get_method_name = prop_get_method_name
    self._prop_set_url = prop_set_url
    self._prop_label = prop_label

  def dispatch_request(self):
    value = getattr(self._device_instance, self._prop_get_method_name)()
    return render_template("prop.html",
      value=value,
      prop_set_url=self._prop_set_url,
      prop_label=self._prop_label)


class RpxPropSetterView(View):
  methods = ["POST"]

  def __init__(self, dev_instance, prop_set_method_name):
    self._device_instance = dev_instance
    self._prop_set_method_name = prop_set_method_name

  def dispatch_request(self):
    value = request.form['value']
    return getattr(self._device_instance, self._prop_set_method_name)(value)


class RpxMultiPropGetterView(View):
  methods = ["GET"]

  def __init__(self, dev_instance, prop_get_method_name, prop_set_url):
    self._device_instance = dev_instance
    self._prop_get_method_name = prop_get_method_name
    self._prop_set_url = prop_set_url

  def dispatch_request(self):
    values = getattr(self._device_instance, self._prop_get_method_name)()
    return render_template("multi_prop.html",
      values=values,
      prop_set_url=self._prop_set_url,
    )

class RpxMultiPropSetterView(View):
  methods = ["POST"]

  def __init__(self, dev_instance, prop_set_method_name, multi_names, prop_set_url):
    self._device_instance = dev_instance
    self._prop_set_method_name = prop_set_method_name
    self._multi_names = multi_names
    self._prop_set_url = prop_set_url

  def dispatch_request(self):
    values = {}
    for multi_name in self._multi_names:
      values[multi_name] = request.form[multi_name]
    response_values = getattr(self._device_instance, self._prop_set_method_name)(**values)
    return render_template("multi_prop.html",
      values=response_values,
      prop_set_url=self._prop_set_url
      )


def convert_to_bool(exp):
  return exp.lower() in ("yes", "true", "t", "1")

#@rpx_device
#class RpxDevice(object):
#
#  def __init__(self, device_id):
#    self.device_id = device_id
#
#  @rpx_command("rpx_activate")
#  def activate(self):
#    return self.drvr_init()
#
#  @rpx_command("rpx_deactivate")
#  def deactivate(self):
#    return self.drvr_uninit()
#
#  def drvr_init(self):
#    raise NotImplementedError("%s not implemented for device ID '%s'" %
#                              (self.drvr_init.__name__, self.device_id))
#
#  def drvr_un_init(self):
#    raise NotImplementedError("%s not implemented for device ID '%s'" %
#                              (self.drvr_uninit.__name__, self.device_id))
#
#  def register_with_host(self, app):
#    for rpx_prop, rpx_prop_get_method_name in self.rpx_getters.iteritems():
#      getter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
#      endpoint_name = "io.%s.prop.get.%s" % (self.device_id, rpx_prop)
#      app.add_url_rule(
#        getter_path,
#        view_func=RpxPropGetterView.as_view(endpoint_name,
#          dev_instance=self,
#          prop_get_method_name=rpx_prop_get_method_name,
#          prop_set_url=getter_path,
#          prop_label=rpx_prop
#        )
#      )
#
#    for rpx_prop, rpx_prop_set_method_name in self.rpx_setters.iteritems():
#      setter_path = "/io/%s/%s" % (self.device_id, rpx_prop)
#      endpoint_name = "io.%s.prop.set.%s" % (self.device_id, rpx_prop)
#      app.add_url_rule(
#        setter_path,
#        view_func=RpxPropSetterView.as_view(endpoint_name,
#          dev_instance=self, prop_set_method_name=rpx_prop_set_method_name)
#      )
#
#    for rpx_command, rpx_command_method_name in self.rpx_commands.iteritems():
#      cmd_path = "/io/%s/cmd/%s" % (self.device_id, rpx_command)
#      endpoint_name = "io.%s.cmd.%s" % (self.device_id, rpx_command)
#      app.add_url_rule(
#        cmd_path,
#        endpoint=endpoint_name,
#        view_func=getattr(self, rpx_command_method_name),
#        methods=['GET', 'POST']
#      )

class RpxDevNotInitializedError(Exception):
  pass

class RpxDevCommError(Exception):
  pass

class RpxPropertyValidationError(Exception):
  pass