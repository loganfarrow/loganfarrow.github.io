from django.shortcuts import render

import requests

def button(request):
    return render(request,'contact.html')

def output(request):
    return "testingnn"

def external(request):
    inp=request.POST.get('param')

