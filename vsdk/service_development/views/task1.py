from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from ..models import *

def task_one(request):
    return render(request, 'task1.xml', content_type='text/xml')

def task_one_submit(request):
    """
    _recording = request.POST['recording']
    _mainCategory = request.POST['mainCategory']
    _subCategory = request.POST['subCategory']
    _voiceMessage = VoiceMessage(mainCategory=_mainCategory, subCategory=_subCategory,
                                 recording=_recording)
                                 """
    return render(request, 'testfinish.xml', content_type='text/xml')

    #_voiceMessage.save()
    #Is this the correct way to address models vars?
    #recording is a filefield.