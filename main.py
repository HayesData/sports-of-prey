import json
import os
import webapp2
from google.appengine.api import images

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

    def post(self):
        self.response.write('test')

        to_composite = []
        for img in json.loads(self.request.body):
            img_path = os.path.join(ROOT_DIR, 'img', img['filename'])
            to_composite.append([img_path, img['x'], img['y'], 1.0, images.TOP_LEFT])

        composite = images.composite(to_composite, 300, 300)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
