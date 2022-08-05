from django.shortcuts import render
from django.core.cache import cache

# Create your views here.

def show_cache(request):
	# movie = cache.get('movie', 'is_none')
	# if movie == 'is_none':
	# 	cache.set('movie', 'Uncharted', 300)
	# 	movie = cache.get('movie')
	movie = cache.get_or_set('movie', 'Uncharted', 300)
	return render(request, 'caching/caching.html', {'movie':movie})

