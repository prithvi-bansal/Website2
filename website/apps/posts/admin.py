from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	model = Post

	list_display = ['id', 'post_title', 'is_good', 'button']
	actions = ['make_good', 'make_bad']

	def make_good(self, request, queryset):
		queryset.update(is_good = True)
	
	def make_bad(self, request, queryset):
		queryset.update(is_good = False)

	def button(self, request):
		# pk = request.id
		post = Post.objects.get(id=1)
		post.is_good = True
		post.save() 
		# import pdb;pdb.set_trace()
		return format_html(
				'<button id="%s">make good</button>' %(post.id)
			)


# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)
