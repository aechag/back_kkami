from django.http import HttpResponse, JsonResponse
import os
from io import BytesIO

import easyocr
from pylab import rcParams

from django.views.decorators.csrf import csrf_exempt

#part to audio
from gtts import gTTS

from detect_text.models import Img_audio
#audio language
language = 'fr'


rcParams['figure.figsize'] = 8, 16
reader = easyocr.Reader(['fr'])

@csrf_exempt
def detectText(request):
    if request.method == 'POST':

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

        id = toAudio2(textfromimg)

        # response = HttpResponse(data, content_type='application/audio/mp3')
        # response['Content-Disposition'] = 'attachment; filename="lots.xlsx"'
        # return response

        return JsonResponse(get_audios(id), safe=False)

    else:
        return HttpResponse('its a get')


#function text to audio
def toAudio(mytext):

    myobj = gTTS(text=mytext, lang=language, slow=False)

    #os.remove("detect_text/files/audio_file.mp3")
    myobj.save("detect_text/files/audio_file.mp3")


def toAudio2(mytext):
    name = "text"
    file_name = '{}.mp3'.format(str(name).lower().replace(' ', '_'))
    b = Img_audio()

    myobj = gTTS(text = mytext, lang=language, slow=False)

    mp3_fp = BytesIO()
    myobj.write_to_fp(mp3_fp)

    b.name = name
    b.audio.save(file_name, mp3_fp)

    b.save()

    return b.id


#function responce with audio
def playAudioFile(request):
    fname="detect_text/files/audio_file.mp3"
    f = open(fname, "rb")

    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)

    return response


def get_audios(id):
    audio = Img_audio.objects.get(id=id)

    url = "http://127.0.0.1:8000/media/" + str(audio.audio)

    return url
