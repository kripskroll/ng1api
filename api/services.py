# 2019-04-02
# Kripskroll
#########################

from urllib import quote
from parent import nG1Parent

class nG1Services(nG1Parent):
	""" This class is for Services."""

	def __init__(self, opener, base_url):
		"""Instance for nGeniusONE Services Constructor

		Arguments :
			opener -- The opener built with Cookie handler and HTTPS context.
			base_url -- The REST API base URL."""

		self.OPENER = opener
		self.API_URL = base_url + '/ncm/services'

	def get(self, type=None):
		"""Used to view services on a nGeniusONE server.

		Arguments :
			no type -- Return all Services (Application and Network).
			type = "application" -- Returns application services.
			type = "network" -- Returns network services.

		Return -- object with request output containing all services. Object.read() to see content. See urllib.open() for associated method to use."""

		if type:
			self.API_URL = self.API_URL + '?type=%s' % type
		
		return self.OPENER.open(self.API_URL)

	def getDetail(self, name):
		"""Used to get service details associated with a service.

		Arguments :
			name -- Return Name of this service.

		Return -- object with request output. Object.read() to see content. See urllib.open() for associated method to use."""

		name = quote(name) # Replace spaces with %20
		self.API_URL = self.API_URL + '/%s' % name
		return self.OPENER.open(self.API_URL)
