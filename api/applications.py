from urllib import quote
from urllib2 import Request
from parent import nG1Parent

class nG1Applications(nG1Parent):
	""" This class is for Applications

	Arguments :
	opener -- The opener built with Cookie handler.
	base_url -- The REST API base URL."""

	def __init__(self, opener, base_url):

		self.OPENER = opener
		self.API_URL = base_url + '/ncm/applications'

	def getApplication(self, app):
		"""Used to view Application being monitored on a nGeniusONE server.

		Arguments :
		app -- all -- For all applications.
		app -- "SAMPLE" -- For "SAMPLE" application definition .

		Return : object with request output. Object.read() to see content. See urllib.open() for associated method usable."""		
		
		if app=="all" :
			return self.OPENER.open(self.API_URL)
		app = quote(arg) # Replace spaces with %20
		url = self.API_URL + '/%s' % app

		return self.OPENER.open(url)

	def addApplication(self, file):
		"""Used to add custom applications to be monitored. The following types of applications can be added through the API: well-known applications, server-based applications, and URL applications.

		Arguments :
		file -- file with XML definition of application."""
		headers = {"Content-Type":"application/xml"}
		req = Request(self.API_URL,file, headers)

		return self.OPENER.open(req)

	def delApplication(self, name):
		"""Delete Application by Name.
		Used to delete a specific custom application, so that it will no longer be monitored by your nGeniusONE server.

		Arguments :
		name -- Name of application to delete"""

		name = quote(name) # Replace spaces with %20
		self.API_URL = self.API_URL + '/%s' % name
		request = Request(self.API_URL)
		request.get_method = lambda: 'DELETE'

		return self.OPENER.open(request)

	def updateApplication(self, file):
		"""curl -X POST –u <username>:<password> -d @input.txt -k https://<server-ip-address>:<ssl-port>/ng1api/ncm/applications"""
		headers = {"Content-Type":"application/xml"}
		req = Request(self.API_URL, file, headers)
		req.get_method = lambda: 'PUT'
		return self.OPENER.open(req)