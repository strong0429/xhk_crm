from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    if not request.session.get('is_login', None):
        return redirect('loged/login/')

    userName = request.session.get('user_name', 'guest')
    return HttpResponse("Hello, %s!" % userName)
