# coding: utf8
# Create your views here.
#import glob
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template.context import RequestContext
#from django.contrib.auth import logout
#from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404


def uLogout(request):
    pass
    #user = request.user #запрашиваем пользователя из запроса (сессии)
    #text="not auth"
    #if user.is_active:
        #logout(request)
        #text = "leave so soon?"
    ##return render_to_response('test.html', {'content': text}, RequestContext(request))
    #return render(request,'test.html', {'content': text})

def uLogin(request):
    pass
    #if request.method == 'POST':
        #loginForm = LoginForm(request.POST)
        #if loginForm.is_valid():
            #user=authenticate(username=loginForm.cleaned_data['uName'],password=loginForm.cleaned_data['uPass'])
            #if user is not None:
                #if user.is_active:
                    #text="wellcome"
                    #return render(request,'test.html', {'content': text})
                #else:
                    #return render('dokladedit.html', {'form': loginForm})
    #loginForm = LoginForm()
    #return render('dokladedit.html', {'form': loginForm})

def uProfile(request):
    return HttpResponseRedirect('/add_lesson/')
