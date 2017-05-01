from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from ..models import *

def task_one(request):
    return render(request, 'task1.xml', content_type='text/xml')