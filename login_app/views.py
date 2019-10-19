from django.shortcuts import render
from django.shortcuts import redirect

from .models import User
from . import forms

# Create your views here.

def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        err_msg = '请输入完整的信息'
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = User.objects.get(name=username)
            except:
                err_msg = '用户不存在'
                return render(request, 'login/login.html', locals())
            if user.password == password:
                return redirect('/index/')
            else:
                err_msg = '密码错误'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())

def register(request):
    pass
    return render(request, 'login/register.html')

def logout(request):
    pass
    return redirect('/login/')
