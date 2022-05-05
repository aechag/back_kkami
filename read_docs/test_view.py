import os

from django.http import FileResponse, HttpResponse
from gtts import gTTS


def get_audios(request):
    fname="read_docs/files/audios"
    f = open(fname, "rb")
    size = fname.size

    #FileResponse(song.audio_file.open())
    # response = HttpResponse()
    # response.write(f.read())
    # response['Content-Type'] = 'audio/mp3'
    # response['Content-Length'] = os.path.getsize(fname)

    response = FileResponse(fname.open())
    response['Content-Type'] = fname.content_type
    response['Content-Length'] = size
    #response["Last-Modified"] = http_date(mtime)

    #----------------------------------------------
    # for TEST
    # --------------------******************---------------***************************----------------
    # for p in pdf.pages:
    #     myText = myText + p.extract_text()

    # ----------------------------------------------------------------
    # toAudioTest(myText)


    return response


#----------------------------------function text to audio
def toAudioTest(mytext):
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)

    os.remove("read_docs/files/test/audio_file.mp3")

    myobj.save("read_docs/files/test/audio_file.mp3")


#-------------------------------function111 test
def playAudioFile(request):
    fname="read_docs/files/test/audio_file.mp3"
    f = open(fname, "rb")

    response = HttpResponse()
    response.write(f.read())
    response['Content-Type'] = 'audio/mp3'
    response['Content-Length'] = os.path.getsize(fname)

    return response


# ***************-----------------------------------------------------------------------
@csrf_exempt
def read_by_id(request):
    pdf_id = request.POST['pdf_id']
    nbr_page = request.POST['nbr_page']

    return JsonResponse(get_audios(nbr_page, pdf_id), safe=False)

    obj = doc.objects.filter(id=pdf_id)

    for o in obj:
        n = o.id

    file_name = "read_docs/files/docs/doc" + str(n) + ".pdf"

    # ----------------------------------------------------------------
    pdf = pdfplumber.open(file_name)

    lines = extractText(pdf)

    i = 0
    for mytext in lines:
        if not (not mytext or re.search("^\s*$", mytext)):
            toAudio(i, mytext)
        i = i + 1

    return HttpResponse(get_audios(nbr_page, i))
