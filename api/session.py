# 2019-04-02
# Stephane Froment
# NETSCOUT Systems Ltd
#########################

import urllib
import urllib2, base64
from parent import nG1Parent

class nG1Session(nG1Parent):
	""" This class is for managing Sessions for stateful connection to nGeniusONE REST API."""

	def __init__(self, opener, base_url, user, passw):
		""" Instance for nGeniusONE Sessions Constructor
		
		Arguments :
			opener -- The opener built with Cookie handler and HTTPS context.
			base_url -- The URL of the nGeniusONE
			user -- User with rights to access REST API
			passw -- Password for User
		"""
		self.OPENER = opener
		self.API_URL = base_url + '/rest-sessions'
		self.USER = user
		self.PASS = passw

	def open(self) :
		""" Open a session.  You do not need to use your credentials once session is open."""

		# Create Basic Auth headers
		req = urllib2.Request(self.API_URL)
		base64string = base64.encodestring('%s:%s' % (self.USER, self.PASS)).replace('\n', '')
		req.add_header('Authorization', 'Basic %s' % base64string)
		 
		return self.OPENER.open(req, data=" ")

	def close(self):
		""" Close a session."""
		return self.OPENER.open(self.API_URL+"/close", data="")
