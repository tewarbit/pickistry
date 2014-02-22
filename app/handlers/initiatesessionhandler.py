import webapp2
import logging

from google.appengine.api import mail
from app.session.picksession import PickSession

class InitiateSessionHandler(webapp2.RequestHandler):
	def post(self):
		emails = self.request.get_all("Email")
		logging.info("Recieved initiate session request with email: %s" % str(emails))

		session = PickSession()
		session.members = emails
		session_key = session.put()

		logging.info("Stored new session with id: %s" % session_key.id())
		for member in session.members:
			mail.send_mail(sender=str(session_key.id()) + "@pickistry.appspotmail.com",
						   to=member,
						   subject="New Pick Session started!",
						   body="Pick a number between 1 and 100")


	def get(self):
		self.response.out.write("This is a response to a GET request. Send a POST to do something interesting")