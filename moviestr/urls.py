from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('playlist',views.playlist,name='playlist'),
    # path('loginn',views.loginn,name='loginn'),
    # path('signupp',views.signupp,name='signupp')
]