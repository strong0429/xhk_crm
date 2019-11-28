from django.shortcuts import render
from django.shortcuts import redirect

from . import models

# Create your views here.

def manage_campus(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    list_campus = models.Campus.objects.all()
    return render(request, 'sys_admin/campus.html', locals())