from django.urls import path
from . import views

urlpatterns = [
    path('', views.newspage, name='newspage'),
    path('main.html', views.newspage, name='newspage'),
    path('offer', views.offerpage, name='offerpage'),
	path('warning', views.warning, name='usermode'),
	# path('about', views.about, name='usermode'),
]
