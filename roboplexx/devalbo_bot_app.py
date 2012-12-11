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
#  return render_template('joystick-drive-absolute-old.html')

@devalbo_bot_app.route('/joystick-original')
def joystick2():
#  return render_template('joystick.html')
  return render_template('joystick-drive-absolute-old.html')

@devalbo_bot_app.route('/joystick-raphael')
def joystick2():
  return render_template('joystick-raphael.html')

@devalbo_bot_app.route('/sliders')
def sliders():
  return render_template('differential-drive.html')

@devalbo_bot_app.route('/form')
def form():
  return render_template('form.html')

