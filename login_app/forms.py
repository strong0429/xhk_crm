from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, \
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=256, \
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    employee = forms.CharField(label='工号', max_length=8, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='用户名', max_length=128, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码', max_length=256, \
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='密码确认', max_length=256, \
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(label='手机', max_length=11, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='住址', max_length=128, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    wechat = forms.CharField(label='微信', max_length=128, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    hobby = forms.CharField(label='爱好', max_length=256, \
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    captcha = CaptchaField(label='验证码')
