"""
settings.py
~~~~~~~~~~~~
 
This module supports configuring the Roboplexx server. If you have to
do much (any?) configuration outside of this file to get a basic server up and
running, something needs to be fixed. 
 
:copyright: (c) 2012 by Albert Boehmler
:license: GNU Affero General Public License, see LICENSE for more details.
"""

import ConfigParser
parser = ConfigParser.SafeConfigParser()
parser.read("rpx_config.ini")

# host name to use for server (see http://flask.pocoo.org/docs/api/)
ROBOPLEXX_HOST_NAME = parser.get("roboplexx", "ROBOPLEXX_HOST_NAME")

# which port to host from
ROBOPLEXX_PORT = int(parser.get("roboplexx", "ROBOPLEXX_PORT"))

DEBUG_MODE_ON = bool(parser.get("roboplexx", "DEBUG_MODE_ON"))
