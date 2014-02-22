from google.appengine.ext import ndb

class PickSession(ndb.Model):
	members = ndb.StringProperty(repeated=True)
	responses = ndb.StringProperty(repeated=True)
