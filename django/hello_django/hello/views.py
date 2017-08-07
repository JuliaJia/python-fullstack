from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.models import User
from django.http import HttpRequest,HttpResponse
from django.template import loader,Template
from hello.models import *


# Create your views here.
def hello(request):
    user_list = User.objects.all()
    value1 = Template('<p style="background-color: #46b8da ">这是一个模板</p>')
    return render_to_response('table.html',locals())


def test(request,id,key):
    # print(key)
    ID = '123'
    Author.objects.get(name=ID)
    return render(request,'table-test.html',locals())

def test2(request,id,key):
    t = loader.get_template('table-test.html')
    c = {'foo':'bar'}
    return HttpResponse(t.render(c,request),content_type='text/html')
    # return redirect('/hello')
