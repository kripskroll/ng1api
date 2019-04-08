# from api/parent.py
class nG1Parent(object):
	""" This class is to refactor methods in every subclasses

	Arguments :
	subType -- The sub-type to address."""
	def getRequestURL(self, subType):
		request_url = self.API_URL
		if subType :
			request_url += '/%s' % subType
		print request_url
		return request_url
