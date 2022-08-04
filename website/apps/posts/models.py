from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User  
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
	post_title = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	post_text = RichTextField(blank=True, null=True)
	# post_text = models.TextField()
	post_image = models.ImageField(upload_to='posts/images/')
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
	likes_count = models.BigIntegerField(default='0')

	# def totallikes(self):
	# 	return self.likes.count()

	def __str__(self):
		return '%s - %s' % (self.post_title, self.author)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	added_on = models.DateTimeField(default=timezone.now)
	body = models.TextField()

	def __str__(self):
		return '%s - %s - %s' % (self.post.post_title, self.author, self.body)

	def get_absolute_url(self):
		return reverse('commentcreate', args=[str(self.post_id)])
