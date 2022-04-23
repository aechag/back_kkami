from django.http import HttpResponse
from django.shortcuts import render
import os
import matplotlib.pyplot as plt
import cv2

import easyocr
from pylab import rcParams
from IPython.display import Image

rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['en'])

def detectText(request):
    textfromimg = ''
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    file_name = "detect_text/aspro.jpg"
    output = reader.readtext(file_name)
    i = 0
    size = len(output)
    while i < size:
        textfromimg = textfromimg + ' ' + output[i][1]
        print(output[i][1])
        i = i + 1

    return HttpResponse(textfromimg)
