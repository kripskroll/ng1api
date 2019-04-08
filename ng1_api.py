import urllib2
from cookielib import CookieJar # Manage Session Cookie for REST API
from api.services import nG1Services
from api.session import nG1Session
from api.applications import nG1Applications
from api.sites import nG1Sites
from api.devices import nG1Devices

class NG1APIObject(object):
	""" nGeniusONE REST API Wrapper.
	
	Arguments :
	host -- nGeniusONE server IP Address or FQDN.
	port -- nGeniusONE server HTTP Port.
	user -- nGeniusONE user login.
	passw -- nGeniusONE user password."""

	def __init__(self, host, port=8080, user=None, passw=None):
		self.USER = user
		self.PASS = passw
		# create OPENER to handle Session Cookie (NSSESSIONID)
		self.CJ = CookieJar()
		self.OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.CJ)) 
		self.BASE_URL = 'http://%s:%s/ng1api' % (host,port)

		self.session = nG1Session(self.OPENER, self.BASE_URL, self.USER, self.PASS)
		self.services = nG1Services(self.OPENER, self.BASE_URL)
		self.applications = nG1Applications(self.OPENER, self.BASE_URL)
		self.sites = nG1Sites(self.OPENER, self.BASE_URL)
		self.devices = nG1Devices(self.OPENER, self.BASE_URL)