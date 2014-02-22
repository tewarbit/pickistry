import logging
import webapp2
import re
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail

from app.session.picksession import PickSession

class LogSenderHandler(InboundMailHandler):
	def receive(self, mail_message):
		logging.info('Received a message from: %(sender)s and to: %(to)s' % {"sender": mail_message.sender, "to": mail_message.to})

		sender = mail_message.sender
		try:
			sender = re.search('<?([^<>]+)>?$',mail_message.sender).group(1)
		except AttributeError:
			logging.info("Failed parsing out sender from: %s" % mail_message.sender)

		
		session_id = mail_message.to.split("@")[0]
		logging.info('Looking up info for session: %s' % session_id)

		session = PickSession.get_by_id(int(session_id))
		logging.info(session)
		if session:
			logging.info(session.members)

		# TODO - check if session responses has already gotten an email from this sender
		session.responses.append(sender)
		session.put()
		if set(session.members) == set(session.responses):
			logging.info("Session is complete. Finishing and email responses")
			for member in session.members:
				mail.send_mail(sender=mail_message.to,
							   to=member,
							   subject="Finished Pick Session",
							   body="The session is finished")



app = webapp2.WSGIApplication([LogSenderHandler.mapping()], debug=True)