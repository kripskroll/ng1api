from urllib import quote
from urllib2 import Request
from parent import nG1Parent

class nG1Devices(nG1Parent):
	""" This class is for Devices

	Arguments :
	opener -- The opener built with Cookie handler.
	base_url -- The REST API base URL."""

	def __init__(self, opener, base_url):

		self.OPENER = opener
		self.API_URL = base_url + '/ncm/devices'

	def relearn(self, name):
		"""Relearn a device

		Arguments :
			name -- Device Name."""

		name = quote(name) # Replace spaces with %20
		url = self.API_URL + '/%s/relearn' % name
		print url
		request = Request(url)

		return self.OPENER.open(request, data=" ")
