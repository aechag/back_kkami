from django.http import HttpResponse
import os

import easyocr
from pylab import rcParams

from django.views.decorators.csrf import csrf_exempt

#part to audio
from gtts import gTTS
#audio language
language = 'fr'


rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['fr'])

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
            i = i + 1

        toAudio(textfromimg)

        # response = HttpResponse(data, content_type='application/audio/mp3')
        # response['Content-Disposition'] = 'attachment; filename="lots.xlsx"'
        # return response

        return playAudioFile(request)

    else:
        return HttpResponse('its a get')


#function text to audio
def toAudio(mytext):

    myobj = gTTS(text=mytext, lang=language, slow=False)

    os.remove("detect_text/files/audio_file.mp3")
    myobj.save("detect_text/files/audio_file.mp3")


#function responce with audio
def playAudioFile(request):
    fname="detect_text/files/audio_file.mp3"
    f = open(fname, "rb")

    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)

    return response
