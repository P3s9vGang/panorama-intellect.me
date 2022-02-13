from django.urls import path
from . import views

urlpatterns = [
    path('', views.usermode, name='usermode'),
    path('main.html', views.usermode, name='usermode')
]
