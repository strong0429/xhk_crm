# sys_admin urls

from django.urls import path

from . import views

urlpatterns = [
    path('campus/', views.manage_campus, name='campus'),
]