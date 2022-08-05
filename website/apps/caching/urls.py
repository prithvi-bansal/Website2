from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
	path('', views.show_cache),
	# path('', cache_page(60)(views.show_cache)),
]
