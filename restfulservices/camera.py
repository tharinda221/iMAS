from flask import Response, request
from flask_restful import Resource
from libs.camera import Camera
from libs.Applications import *
from backendData.common.constants import *
from backendData.database.operations import *


def gen(camera, obj):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame(obj)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


class camera(Resource):
    def get(self):
        obj = getiMASAppDetailsById(common.appID)
        return Response(gen(Camera(), obj),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
