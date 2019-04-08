import urllib
import urllib2, base64
from parent import nG1Parent

class nG1Session(nG1Parent):
	""" This class is for managing Sessions for stateful connection to nGeniusONE REST API."""
	def __init__(self, opener, base_url, user, passw):
		self.OPENER = opener
		self.API_URL = base_url + '/rest-sessions'
		self.USER = user
		self.PASS = passw

	def openSession(self) :
		""" Open a session.  You do not need to use your credentials once session is open."""

		# Create Basic Auth headers
		req = urllib2.Request(self.API_URL)
		base64string = base64.encodestring('%s:%s' % (self.USER, self.PASS)).replace('\n', '')
		req.add_header('Authorization', 'Basic %s' % base64string)
		 
		return self.OPENER.open(req, data=" ")

	def closeSession(self):
		""" Close a session."""
		return self.OPENER.open(self.API_URL+"/close", data="")
