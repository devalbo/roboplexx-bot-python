__author__ = 'ajb'

from flask import Blueprint, render_template
import settings, jinja2

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
  return render_template('joystick-drive-absolute-old.html',
    {"camera_html_tag": settings.CAMERA_HTML_TAG})

@devalbo_bot_app.route('/joystick-raphael')
def joystick2():
  return render_template('joystick-raphael.html',
    camera_html_tag=jinja2.Markup(settings.CAMERA_HTML_TAG))

@devalbo_bot_app.route('/sliders')
def sliders():
  return render_template('differential-drive.html')

@devalbo_bot_app.route('/form')
def form():
  return render_template('form.html')

@devalbo_bot_app.route('/phone')
def phone_ui():
  return render_template('mobile.html',
    camera_html_tag=jinja2.Markup(settings.CAMERA_HTML_TAG),
    camera_server_url=settings.CAMERA_SERVER_URL)

@devalbo_bot_app.route('/phone2')
def phone_ui2():
  return render_template('mobile2.html')
