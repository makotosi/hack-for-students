#!/usr/bin/env python
#
# Copyright 2012 Google Ambassadors

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
  def get(self):
    template_values = {
      'title': 'Hack for Students',
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    html = template.render(path, template_values)
    self.response.out.write(html)

def main():
    application = webapp.WSGIApplication([('/', MainPage)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
