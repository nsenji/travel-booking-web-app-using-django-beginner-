from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index")
] 


'''NOTE this is the fisrt thing that  the web app will execute so everything starts from here'''
