from django.shortcuts import render
from django.http import HttpResponse
import datetime

def list_info(request):
    agora = datetime.datetime.now()
    html = "<html><body>Testando! Agora é: %s</body></html>" % agora
    return HttpResponse(html)
