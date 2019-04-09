# 2019-04-02
# Stephane Froment
# NETSCOUT Systems Ltd
#########################

from urllib import quote
from urllib2 import Request
from parent import nG1Parent

class nG1Sites(nG1Parent):
	""" This class is for Sites"""
	
	def __init__(self, opener, base_url):
		"""Instance for nGeniusONE Sites Constructor
		
		Arguments :
			opener -- The opener built with Cookie handler and HTTPS context.
			base_url -- The REST API base URL.
		"""
		self.OPENER = opener
		self.API_URL = base_url + '/ncm/sites'

	def get(self, arg):
		
		if arg=="all" :
			return self.OPENER.open(self.API_URL)
		arg = quote(arg) # Replace spaces with %20
		self.API_URL = self.API_URL + '/%s' % arg

		return self.OPENER.open(self.API_URL)

	def add(self, arg):
		# Add multiple sites or specific site using same way by passing full XML/JSON
		
		headers = {"Content-Type":"application/xml"}
		req = Request(self.API_URL,arg, headers)

		return self.OPENER.open(req)

	def update(self, arg):
		# Update multiple sites or specific site using same way by passing full XML/JSON

		return self.OPENER.open(self.API_URL, arg)

	def delete(self, arg):
		# Delete multiple sites or specific site using same way by passing full XML/JSON
		
		arg = quote(arg) # Replace spaces with %20
		self.API_URL = self.API_URL + '/%s' % arg
		request = Request(self.API_URL)
		request.get_method = lambda: 'DELETE'

		return self.OPENER.open(request)