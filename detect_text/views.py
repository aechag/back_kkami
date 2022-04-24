from django.http import HttpResponse
from django.shortcuts import render
import os
import matplotlib.pyplot as plt
import cv2

import easyocr
from pylab import rcParams
from IPython.display import Image
#import magic
import imghdr

from detect_text.forms import UploadFileForm

from django.views.decorators.csrf import csrf_exempt

rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en'])

@csrf_exempt
def detectText(request):
    if request.method == 'POST':
        # form = UploadFileForm()
        textfromimg = ''
        os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

        # file_name = "detect_text/aspro.jpg"
        file_name = request.FILES['image']
        data = file_name.seek(0)
        data0 = file_name.read()

        output = reader.readtext(data0)
        i = 0
        size = len(output)
        while i < size:
            textfromimg = textfromimg + ' ' + output[i][1]
            # print(output[i][1])
            i = i + 1

        return HttpResponse(textfromimg)

    else:
        return HttpResponse('its a get')