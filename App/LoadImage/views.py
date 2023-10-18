from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpRequest
from django.http.response import StreamingHttpResponse
from django.template import Template, Context
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.conf import settings
from .models import Image, ThresholdData
from .forms import ImageForm, ThresholdForm, HSVRangeForm
from App.LoadImage.BasicImageProcessing.basic_ip import *
from .camera import Webcam

import os
import datetime
import cv2
import numpy as np



TEMPLATES = os.path.join(os.getcwd(),'App/LoadImage/templates')


# Funciones y clases chimbitas

def save_imageArray_to_model(imgArray):
    _,imEncoded = cv2.imencode('.png',imgArray)
    imgfile = ContentFile(imEncoded)
    editableImage = Image.objects.get(id=3)
    editableImage.image2analysis.save('actual_edit.png', imgfile, save=True)




# Metodos de vistas 

def home(request: HttpRequest): # Vista
    form = ImageForm()
    if request.method == "POST":
        actualImage = Image.objects.get(id=2)
        editImage = Image.objects.get(id= 3)
        formUpdate = ImageForm(request.POST,request.FILES,instance = actualImage)
        formEditImg = ImageForm(request.POST,request.FILES,instance = editImage)
        if formUpdate.is_valid() and formEditImg.is_valid():
            formUpdate.save()
            formEditImg.save()
        updatedImage = Image.objects.get(id=2)
    else:
        updatedImage = Image.objects.get(id=2)
        
    return render(request, 'loadImg.html', {'form': form, 'image':updatedImage})

def thresholdOp(request: HttpRequest):
    tform = ThresholdForm()
    upperThres = None
    lowerThres = 0
    if request.method == 'POST':
        tform = ThresholdForm(request.POST)
        if tform.is_valid():
            upperThres = int(request.POST['upperThres'])
            lowerThres = int(request.POST['lowerThres'])

            tform.save(commit=False)

    originalImage = Image.objects.get(id=2)
    img2edit = cv2.imread(originalImage.image2analysis.path)
    if img2edit is not None and upperThres is not None:
        # TODO: Terminar código para mostrar el historial de la imagen con las barras denotando el rango usado
        #histr = cv2.calcHist([img2edit],[0],None,[256],[0,256])
        ######################################################
        imgProcessor = ImageProcessor(img2edit)
        imgProcessor.turn_image_to_gray()
        editedImg = imgProcessor.apply_range(upperThres, lowerThres, getMask=True)
        save_imageArray_to_model(editedImg)

    updatedImage = Image.objects.get(id=3)
    return render(request, 'thresholdPage.html', {'form':tform, 'image': updatedImage,})
    
def color_range(request: HttpRequest):
    if request.method == 'POST':
        hsvform = HSVRangeForm(request.POST)
        if hsvform.is_valid():
            hu = int(request.POST['hu'])
            su = int(request.POST['su'])
            vu = int(request.POST['vu'])
            hl = int(request.POST['hl'])
            sl = int(request.POST['sl'])
            vl = int(request.POST['vl'])

            originalImage = Image.objects.get(id=2)

            imgProcessor = ImageProcessor (cv2.imread(originalImage.image2analysis.path))
            imgProcessor.turn_image_to_HSV()
            imgProcessor.apply_range([hu,su,vu],[hl,sl,vl],inner=False)
            hsvFiltered = imgProcessor.get_image_procesed()


            save_imageArray_to_model(hsvFiltered)

    else:
        hu = 180
        su = 255
        vu = 255
        hl = 0
        sl = 0
        vl = 0
        hsvform = HSVRangeForm()
    
    updatedImage = Image.objects.get(id=3)

    values = {
        'hu':hu,
        'su':su,
        'vu':vu,
        'hl':hl,
        'sl':sl,
        'vl':vl,
    }

    
    return render(request, 'colorRanges.html', {'form':hsvform, 'image': updatedImage, 'values':values})



def streaming_webcam (request):
    return render(request, 'streaming.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def webcam_feed (request):
    return StreamingHttpResponse(gen(Webcam()),
                                    content_type ='multipart/x-mixed-replace; boundary=frame')
