
import numpy as np
import cv2
import matplotlib.pyplot as plt
from .tracebacks_ip import ImageShapeException

class ImageProcessor:

    def __init__ (self, image2process, channels = 'BGR'):
        if channels != 'BGR':
            self.image = cv2.cvtColor(image2process, cv2.COLOR_RGB2BGR)
        else:
            self.image = image2process


        self.original = np.copy(self.image)
        self.imageProcesed = np.copy(self.image)

        self.turnedHSV = False
        
        
    def get_image_procesed (self):
        self.turn_image_processed_to_BGR()
        return self.imageProcesed

    def get_image_original(self):
        return self.original
    

    def get_imageChannel_1(self):
        return self.original[:,:,0]
    
    def get_imageChannel_2(self):
        return self.original[:,:,1]
    
    def get_imageChannel_3(self):
        return self.original[:,:,2]

    def show_image_procesed (self, waitkey=0, windowTitle= 'Image', destroAllWindows=True):
        self.turn_image_processed_to_BGR()
        cv2.imshow(windowTitle, self.imageProcesed)
        cv2.waitKey(waitkey)
        if destroAllWindows:
            cv2.destroyAllWindows()


    def turn_image_to_HSV (self):
        self.turnedHSV = True
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
    
    def turn_image_to_gray(self):
        self.turnedGray = True
        self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
    
    def turn_image_to_channel (self, channelNumber):
        self.image = np.copy(self.image[:,:,channelNumber])
    
    def turn_image_processed_to_BGR(self):
        if self.turnedHSV:
            self.imageProcesed = cv2.cvtColor(self.imageProcesed, cv2.COLOR_HSV2BGR)
            self.turnedHSV = False
        elif self.turnedGray:
            self.imageProcesed = cv2.cvtColor(self.imageProcesed, cv2.COLOR_GRAY2BGR)
            self.turnedGray = False
        else:
            pass



    def apply_simple_threshold(self, thres, maxValue , cv2Operation,adaptive = None, specifyChannel = None):
        # method to do threshold, if need an adaptive method specify by a tuple or list 
        # adaptive = (adaptiveCV2operation, blockSize, C constant) more info opencv documentation
        #  https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
        
        # If need apply the operation in a specific channel of the original image,
        # asign the number of the channel in the variable name specifyChannel 

        if len(self.image.shape) > 2:
            mensaje = """La operación de Threshold solo admite imágenes de un (1) solo canal.
Se debe realizar primero cualquiera de las opraciones:
-turn_image_to_gray()
-turn_image_to_channel()"""

            raise ImageShapeException(mensaje)


        if adaptive is not None:
            self.imageProcesed = cv2.adaptiveThreshold(self.image,maxValue, adaptive[0], cv2Operation, adaptive[1],adaptive[2])
        else:
            _ , self.imageProcesed = cv2.threshold(self.image,thres,maxValue, cv2Operation)


    def apply_range(self, upperThres, lowerThres, inner = True, getMask = False):
        # If need to apply the operation to a gray image, first do turn_image_to_gray()
        # If need to apply the operation to a HSV image, first do turn_image_to_HSV()
        # upper and lower thres must be tuple, list or float

        if len(self.image.shape) == 2 :
            try:
                uthresLen= len(upperThres)
                lthresLen= len(lowerThres)
                if uthresLen > 1 or lthresLen > 1:
                    mensaje = """La imagen solo tiene un canal y alguno de los umbrales tiene más de una (1) sola entrada"""
                    raise ImageShapeException(mensaje)
            except TypeError:
                pass

        elif len(self.image.shape) == 3:
            try:
                uthresLen= len(upperThres)
                lthresLen= len(lowerThres)
                if uthresLen != 3 or lthresLen != 3:
                    raise TypeError
            except TypeError:
                mensaje = """La imagen tiene 3 canales y alguno de los umbrales no tiene el número correcto de entradas"""
                raise ImageShapeException(mensaje)

                

        mask = cv2.inRange(self.image, np.array(lowerThres) , np.array(upperThres))
        if inner :
            self.imageProcesed = cv2.bitwise_and(self.image,self.image, mask = mask)
        else:
            mask = cv2.bitwise_not(mask)
            self.imageProcesed = cv2.bitwise_and(self.image,self.image, mask = mask)
        
        if getMask:
            return mask

