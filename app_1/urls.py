from django.urls import path

from . import views
# from views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('showresult', views.showresult, name='showresult'),
    path('testing', views.testing, name='testing'),


]