from flask_restful import Resource
from flask import Response
from libs.camera import Camera

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


class camera(Resource):
    def get(self):
        return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
