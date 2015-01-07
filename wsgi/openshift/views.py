import os
from django import VERSION
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/home.html', {'django_version': '.'.join([str(i) for i in VERSION[:3]])})
