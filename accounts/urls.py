from django.urls import path
from . import views


urlpatterns= [
    path('signin/', views.custom_login, name= "signin"),
    path('logout/', views.logout, name= "logout"),
]