import cv2
import numpy as np
import urllib.request
from  django.conf import settings


class Webcam(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()

        ret, jpgImg = cv2.imencode('.jpg', image)
        return jpgImg.tobytes()
