from os import path
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext.webapp.template import render
import webapp2

class Greeting(db.Model):
    author = db.UserProperty()
    something_random = db.StringProperty(multiline=False)
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):

  def get(self):
    self.response.headers['Content-Type'] = 'text/html'

    user = users.get_current_user()
    if user:
        self.response.write(
            'Hello %s [<a href=%s>sign out</a>]' % (user.nickname(), users.create_logout_url(self.request.uri))
        )
    else:
        #self.response.write(
        #    'Hello World! [<a href=%s>sign in</a>]' % users.create_login_url(self.request.uri)
        #)
        self.redirect(users.create_login_url(self.request.uri))
        return
    self.response.write('<h1>My GuestBook</h1><ul>')
    greetings = Greeting.all()
    for greeting in greetings:
        # greeting.delete()
        if not greeting.author:
            greeting.author = "N/A"
        if not greeting.something_random:
            greeting.something_random = ""
        self.response.write('<li><b>%s</b> %s<br />%s' % (greeting.author, greeting.something_random, greeting.content))
    self.response.write('''
        </ul><hr>

        <form action="/sign" method=post>
        <label for="content"><b>Sign the guestbook</b></label><br />
        <textarea id="content" name="content" rows="3" cols="60"></textarea>
        <br /><br /><label for="something_random"><b>Favorite emoji</b></label><br />
        <input id="something_random" name="something_random" placeholder="Enter your favorite emoji..." />
        <br /><br /><input type=submit value="Sign Guestbook">
        </form>
    ''')

class ClearData(webapp2.RequestHandler):
    def get(self):
        if users.is_current_user_admin():
            greetings = Greeting.all()
            for greeting in greetings:
                greeting.delete()
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write('<b>Stored signatures deleted.</b>')
        else:
            self.error(403)
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write('<h1>Forbidden</h1><p>You don\'t have access to this location.</p>')


class GuestBook(webapp2.RequestHandler):
  def post(self):
    greeting = Greeting()
    user = users.get_current_user()
    if user:
        greeting.author = user
    greeting.content = self.request.get('content')
    greeting.something_random = self.request.get('something_random')
    greeting.put()
    self.redirect('/')
    # self.response.write(
    #   '<h2>You wrote:</h2> %s' % self.request.get('content')
    # )

APP = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign', GuestBook),
    ('/clear', ClearData),
], debug=True)

