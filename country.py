import cgi
import urllib
import webapp2
import random

from google.appengine.ext import db
from google.appengine.api import users

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Country(db.Model):
  index = db.FloatProperty()
  name = db.StringProperty()
  capital = db.StringProperty()
  continent = db.StringProperty()


class MainPage(webapp2.RequestHandler):
  def get(self):
    # Try and read a country from a parameter
    country_param = self.request.get('c')
    if country_param == "":
    	rand_num = random.random()
    	country = Country.all().order('index').filter('index >=', rand_num).get()
    	if country is None:
    		country = Country.all().order('index').get()
    else:	
    	country = Country.all().filter('name =', country_param).get()
    	if country is None:
    		country = Country.all().order('index').get()

    template_values = {
      'country': country
    }

    template = jinja_environment.get_template('country.html')
    self.response.out.write(template.render(template_values))

  def post(self):
    # Check if the country is already there before adding a new one
    country = Country.all().filter('name =', self.request.get('country')).get()
    if country is None:
    	country = Country()
    	country.index = random.random()
    	country.name = self.request.get('country')
    	country.capital = self.request.get('capital')
    	country.continent = self.request.get('continent')
    	country.put()
    
    template = jinja_environment.get_template('country.html')
    self.response.out.write(template.render({'country': country}))

class Atlas(webapp2.RequestHandler):
  def post(self):
    country = Country()
    country.index = random.random()
    country.name = self.request.get('country')
    country.capital = self.request.get('capital')
    country.continent = self.request.get('continent')
    country.put()
    self.redirect('/')

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/add', Atlas)
])