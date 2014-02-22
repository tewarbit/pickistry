import webapp2

from app.handlers.initiatesessionhandler import InitiateSessionHandler

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect('app/static/index.html')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/initiate', InitiateSessionHandler)
], debug=True)