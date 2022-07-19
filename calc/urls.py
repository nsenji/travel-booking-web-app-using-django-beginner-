from django.urls import path
from . import views

urlpatterns = [
    path('add',views.add),
    path('',views.home)
] 


'''NOTE this is the fisrt thing that  the web app will execute so everything starts from here'''
