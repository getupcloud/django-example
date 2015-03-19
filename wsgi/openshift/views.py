import os
from django import VERSION
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseNotFound

from tasks import *

def home(request):
    return render_to_response('home/home.html', {'django_version': '.'.join([str(i) for i in VERSION[:3]])})

def task(request, taskname):
    if taskname == 'add':
        x, y = int(request.REQUEST['x']), int(request.REQUEST['y'])
        add.delay(x, y)
    elif taskname == 'mul':
        x, y = int(request.REQUEST['x']), int(request.REQUEST['y'])
        mul.delay(x, y)
    elif taskname == 'xsum':
        numbers = map(int, request.REQUEST['numbers'].split(','))
        xsum.delay(numbers)
    elif taskname == 'sleep':
        s = int(request.REQUEST['seconds'])
        sleep.delay(s)
    else:
        return HttpResponseNotFound('Unknown task name: %s' % taskname)

    return HttpResponse('OK\n')
