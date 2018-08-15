from django.http import HttpResponse
from django.shortcuts import render_to_response

def search_form(request):
    return render_to_response('search.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'You Search Content:' + request.GET['q']
    else:
        message = 'Input Null Form'
    return HttpResponse(message)

