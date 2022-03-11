from django.urls import path
from . import views

urlpatterns = [
    path('', views.newspage, name='newspage'),
    path('main.html', views.newspage, name='newspage'),
    path('offer', views.offerpage, name='offerpage'),
	path('warning', views.warning, name='usermode'),
	path('requirements', views.requirements, name='usermode'),
	path('donate', views.donate, name='usermode'),
	path('confirmation', views.confirmation, name='usermode'),
	# path('about', views.about, name='usermode'),
]
