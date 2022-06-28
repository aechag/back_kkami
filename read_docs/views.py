import os
from io import BytesIO
from unicodedata import name

from django.http import HttpResponse, FileResponse, JsonResponse

# Create your views here.
import pdfplumber
import re

from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS

from read_docs.models import doc, Audio


language = 'fr'

@csrf_exempt
def pdf_to_audio(request):
    if request.method == 'POST':
        file_name = request.FILES['doc']
        num_pdf = save(file_name)

        pdf = pdfplumber.open(file_name)

        i = 0
        #--*************BY_PAGE
        for p in pdf.pages:
            if not (not p.extract_text() or re.search("^\s*$", p.extract_text())):
                toAudio(i, p.extract_text(), num_pdf)
            i = i + 1

        #--**************BY_LINE
        # lines = extractText(pdf)
        # for mytext in lines:
        #     if not (not mytext or re.search("^\s*$", mytext)):
        #         toAudio(i, mytext)
        #     i = i + 1

        return JsonResponse(get_audios(0,num_pdf), safe=False)
        # return HttpResponse(get_audios(0, i))

#--------------------------------------------
def extractText(pdf):
    line_list = []

    pages = len(pdf.pages)

    for i in range(pages):

        # Creating a page object
        pageObj = pdf.pages[i]

        # Printing Page Number
        print("Page No: ", i)

        # Extracting text from page
        text = pageObj.extract_text().split("\n")

        # lines are stored into list
        for i in range(len(text)):
            line_list.append(text[i])


    # closing the pdf file object
    pdf.close()

    return line_list

def toAudio(nbr, mytext, num_pdf):
    name = "page" + str(nbr)
    file_name = '{}.mp3'.format(str(name).lower().replace(' ', '_'))
    b = Audio()

    myobj = gTTS(text = mytext, lang=language, slow=False)

    mp3_fp = BytesIO()
    myobj.write_to_fp(mp3_fp)

    b.name = name
    b.num_pdf = num_pdf
    b.audio.save(file_name, mp3_fp)

    b.save()

def get_audios(nbr_start, num_pdf):
    list_url = []
    audios = Audio.objects.all().filter(num_pdf=num_pdf)
    
    for n in audios:
        url = "http://192.168.124.105:8000/media/" + str(n.audio)
        list_url.append(url)
    list_url = list_url[nbr_start:]

    return list_url

#-------------------------------------------*********---------------------------------------------------
#------------------save
def save(file):
    b = doc(path="read_docs/files/docs/doc.pdf", name="pdf nom")
    b.save()

    path = "read_docs/files/docs/doc" + str(b.id) + ".pdf"
    doc.objects.filter(id=b.id).update(path=path, name="pdf"+str(b.id))

    with open(path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

    # x = path.split("/ ")[-1])
    return b.id

#-----------------all
def get_all(request):
    data = list(doc.objects.values())
    return JsonResponse(data, safe=False)
#------------------------readpdf_by_id
@csrf_exempt
def read_by_id2(request):
    pdf_id = request.POST.get('pdf_id', False)
    nbr_page = request.POST.get('nbr_page', False)

    return JsonResponse(get_audios(nbr_page, pdf_id), safe=False)
@csrf_exempt
def read_by_id(request):
    pdf_id = request.POST['pdf_id']
    nbr_page = request.POST['nbr_page']

    return JsonResponse(get_audios(int(nbr_page), pdf_id), safe=False)

# *222
@csrf_exempt
def read_by_pdf(request):
    pdf_id = request.POST['pdf_id']
    d = doc.objects.get(id=pdf_id)

    return JsonResponse(get_audios(int(d.nbr_page_read), pdf_id), safe=False)
#-------------------update
@csrf_exempt
def update_nbr_page(request):
    
    doc.objects.filter(id=request.POST.get('id', False)).update(nbr_page_read=request.POST.get('nbr_page', False))
    return JsonResponse({'status': 'ok'})