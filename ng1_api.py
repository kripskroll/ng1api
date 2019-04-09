# 2019-04-02
# Kripskroll
#########################

import urllib2
import ssl
from cookielib import CookieJar # Manage Session Cookie for REST API
from api.services import nG1Services
from api.session import nG1Session
from api.applications import nG1Applications
from api.sites import nG1Sites
from api.devices import nG1Devices

class NG1APIObject(object):
	""" nGeniusONE REST API Wrapper."""

	def __init__(self, host, port=8443, user=None, passw=None, https=False ,secure=False):
		""" Instance of an nG1 REST API Constructor

		Arguments :
			host -- nGeniusONE server hostname or IP
			port -- nGeniusONE server port. Default = 8443
			user -- User with rights to access REST API
			passw -- Password for User
			https -- if you want to use HTTPS put it as True (https=True)
			secure -- Need to check Certificate validity. Default = false."""

		self.USER = user
		self.PASS = passw
		# create OPENER to handle Session Cookie (NSSESSIONID)
		self.CJ = CookieJar()
		
		if not https:
			print ("https = ", https)
			self.OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.CJ))
			self.BASE_URL = 'http://%s:%s/ng1api' % (host,port)
		else:			
			self.CONTEXT=ssl.create_default_context()
			if not secure:
				# create context to manage SSL and NO CERTIFICATE Error
				self.CONTEXT = ssl._create_unverified_context()
			self.OPENER = urllib2.build_opener(urllib2.HTTPSHandler(context=self.CONTEXT),urllib2.HTTPCookieProcessor(self.CJ))
			self.BASE_URL = 'https://%s:%s/ng1api' % (host,port)
		self.session = nG1Session(self.OPENER, self.BASE_URL, self.USER, self.PASS)
		self.services = nG1Services(self.OPENER, self.BASE_URL)
		self.applications = nG1Applications(self.OPENER, self.BASE_URL)
		self.sites = nG1Sites(self.OPENER, self.BASE_URL)
		self.devices = nG1Devices(self.OPENER, self.BASE_URL)
