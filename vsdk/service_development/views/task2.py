from django.shortcuts import render

def task_two(request):
    return render(request, 'task2.xml', content_type='text/xml')
