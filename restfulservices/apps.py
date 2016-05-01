from flask import Response
from flask_restful import Resource
from libs.camera import Camera
from backendData.applications.motionDetector.motionDetector import *

def gen(motion):
    """Video streaming generator function."""
    while True:
        frame = motion.movingImageGenarating()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


class motionDetector(Resource):
    def get(self):
        # return Response(motion_detector(Camera().getCam()), mimetype='text/plain')
        return Response(gen(MotionDetector()), mimetype='multipart/x-mixed-replace; boundary=frame')
