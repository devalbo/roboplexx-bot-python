__author__ = 'ajb'

from flask import Blueprint, render_template

devalbo_bot_app = Blueprint('app', __name__,
  template_folder='templates')

@devalbo_bot_app.route('/')
def index():
  return joystick()

@devalbo_bot_app.route('/joystick')
def joystick():
  return render_template('joystick.html')

@devalbo_bot_app.route('/sliders')
def sliders():
  return render_template('sliders.html')

@devalbo_bot_app.route('/form')
def form():
  return render_template('form.html')

