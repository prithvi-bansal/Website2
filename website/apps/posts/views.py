from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone, dateformat
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
import json

import logging
logger = logging.getLogger('main')

# Create your views here.

@login_required
def PostLike(request):
	if request.POST.get('action') == 'post':
		result = ''
		id1 = int(request.POST.get('post_id'))
		post = get_object_or_404(Post, id=id1)
		is_liked = False
		if post.likes.filter(id=request.user.id).exists():
			post.likes.remove(request.user)
			post.likes_count -= 1
			result = post.likes_count
			post.save()
			is_liked = False
		else:
			post.likes.add(request.user)
			post.likes_count += 1
			result = post.likes_count
			post.save()
			is_liked = True
		return JsonResponse({'result':result, 'is_liked':is_liked })
	else:
		return HttpResponseRedirect(reverse('postview'))


class PostListView(ListView):
	model = Post
	template_name = 'posts/postview.html'

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data()
		context = Post.objects.all().order_by('id')

		# Paginator
		p = Paginator(context, 2)
		page = self.request.GET.get('page')
		posts = p.get_page(page)

		is_liked = False
		user = self.request.user.id
		post = Post.objects.values('id')
		for post in post:
			post = post['id']
			# print(post)
			if Post.objects.filter(likes__id=user, id=post).exists():
				is_liked = True
				# print('not working')
			else:
				is_liked = False
				# print('not working-2')				
		return { 'context':context, 'is_liked' : is_liked, 'posts' : posts }


class PostUserView(ListView):
	model = Post
	template_name = 'posts/postuserview.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_user = self.request.user
		context = Post.objects.filter(author = current_user)
		context = {'context':context}
		logger.info('Hello')
		return context

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	# fields = ['post_title', 'post_text', 'post_image']
	success_url = '/post'
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'posts/postupdate.html'
	success_url = '/post'

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'posts/postdelete.html'
	success_url = '/home/dashboard'

class CommentCreateView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'posts/comment.html'

	def AddComment(request):
		if request.POST.get('action') == 'post':
			post = int(request.POST.get('post_id'))
			post1 = Post.objects.get(id=post)
			author = request.user.username
			added_on = timezone.now()
			body = request.POST.get('comment')
			comment = Comment.objects.create(post = post1, body = body, author = request.user)
			comment.save()
			comment_id = comment.id
			data = {
				'body' : body,
				'author' : author,
				'added_on' : added_on,
				'comment_id' : int(comment_id),
			}
			return JsonResponse(data)
		else:
			return HttpResponseRedirect('/post')

	def get_success_url(self, **kwargs):
		return self.object.get_absolute_url()

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context = Post.objects.filter(id=self.kwargs['pk'])
		context = {'context':context}
		return context


class CommentUpdateView(UpdateView):
	model = Comment
	form_class = CommentForm
	template_name = 'posts/commentupdate.html'
	success_url = '/post'


class CommentDeleteView(DeleteView):
	model = Comment
	template_name = 'posts/commentdelete.html'
	success_url = '/post'


