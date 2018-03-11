from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect  #重定向
from django.urls import reverse
from django.shortcuts import render   #渲染模板
import psutil, time, json

from . import information

def index(request):

    return render(request, 'home.html')

def manage(request):
    return render(request, '.html')

def notification(request):
    return render(request, 'notification.html')

def task(request):
    return render(request, 'task.html')

def task_manage(request):
    List = information.taskmanage()
    return render(request, 'Task_Manager.html', {'List':List})

def cpu(request):

    return render(request,'cpu.html')



def about(request):
    return render(request, 'about.html')
# def console(request):
#     js_code = information.get_mem()
#     return render(request, 'console.html', {'js_code':js_code})
def doc(request):
    return render(request, 'doc.html')


def test(request):

    return render(request, 'test.html')

def ajax_list(request):
    a = information.taskmanage()
    return JsonResponse(a, safe=False)

def cpu_percent(request):
    name_dict = information.get_cpu_percent()
    return JsonResponse(name_dict, safe=False)

def auto_change_addr(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# def taskmanage():
#     data = information.taskmanage()
#     all_program = json.dumps(data)
#     print(all_program)
# taskmanage()

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
    #http://127.0.0.1:8080/add/?a=33&b=44
'''
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
    #http://127.0.0.1:8080/add2/11/22/
def view_name(request):
    return render(request, 'home.html')
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))
    #旧链接重定向至新链接
def test(request):
    position = u'HOME'
    return render(request, 'test.html', {'position':position})
'''