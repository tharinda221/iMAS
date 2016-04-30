#!/usr/bin/env python
import os

from flask import Flask
from restfulservices.index import *
from restfulservices.camera import *
from restfulservices.about import *
from restfulservices.apps import *

from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)
app.secret_key = os.urandom(24)

api.add_resource(main, '/', endpoint='/')
api.add_resource(camera, '/video_feed', endpoint='/video_feed')
api.add_resource(about, '/about', endpoint='/about')
api.add_resource(runApplication, '/runApplication/<appId>')
api.add_resource(motionDetector, '/motionDetector', endpoint='/motionDetector')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
