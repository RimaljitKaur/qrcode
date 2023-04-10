from django.shortcuts import render
import pyqrcode
from pyqrcode import QRCode
from .models import *


def qrCode(request):
    context={}
    if request.method=="POST":
        text=request.POST['qr_text']
        urlpath = pyqrcode.create(text)
        name=request.POST['name']
        url = urlpath.svg(name+'.svg',scale=8)
        context["svg"] = url
        Code.objects.create(qr_code=url,qr_name=name)
    else:
        pass
    return render(request,"index.html",{'data':context})
