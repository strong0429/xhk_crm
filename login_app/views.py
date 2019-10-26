from django.shortcuts import render
from django.shortcuts import redirect

from sys_admin.models import Employee
from .models import User
from . import forms

# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

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
                request.session['is_login'] = True
                request.session['user_id'] = user.id 
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                err_msg = '密码错误'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    user_name = request.session.get('reg_user_name', '')
    login_form = forms.UserForm(initial={'username': user_name})
    return render(request, 'login/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    
    if request.method == 'POST':
        err_msg = '请检查输入信息'
        register_form = forms.RegisterForm(request.POST)
        if not register_form.is_valid():
            return render(request, 'login/register.html', locals())

        employee_id = register_form.cleaned_data.get('employee')
        if not employee_id.isdigit():
            err_msg = '工号格式错误！应由1~4位数字组成'
            return render(request, 'login/register.html', locals())

        password = register_form.cleaned_data.get('password')
        password1 = register_form.cleaned_data.get('password1')
        if password != password1:
            err_msg = '输入密码不一致'
            return render(request, 'login/register.html', locals())

        try:
            employee_id = int(employee_id)
            employee = Employee.objects.get(pk=employee_id)
        except:
            err_msg = '输入工号未注册'
            return render(request, 'login/register.html', locals())

        username = register_form.cleaned_data.get('username')
        same_name_user = User.objects.filter(name=username)
        if same_name_user:
            err_msg = '输入用户名已存在'
            return render(request, 'login/register.html', locals())

        new_user = User()
        new_user.name = username
        new_user.password = password
        new_user.employee = employee
        new_user.mobile = register_form.cleaned_data.get('mobile')
        new_user.email = register_form.cleaned_data.get('email')
        new_user.wechat = register_form.cleaned_data.get('wechat')
        new_user.address = register_form.cleaned_data.get('address')
        new_user.hobby = register_form.cleaned_data.get('hobby')

        try:
            new_user.save()
            request.session['reg_user_name'] = new_user.name
            return redirect('/login/')
        except:
            err_msg = '注册失败'
            return render(request, 'login/register.html', locals())

    register_form = forms.RegisterForm()
    no_star = ['住址', '邮箱', '微信', '爱好']
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')
