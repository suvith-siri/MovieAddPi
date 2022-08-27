from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path("signupp",views.signupp,name="signupp"),
    path("loginn",views.loginn,name="loginn"),
    path('afterlog',views.afterlog,name="afterlog"),
]