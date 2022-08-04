from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['post_title', 'post_text', 'post_image']

		widgets = {
			'post_title' : forms.TextInput(attrs={'class':'form-control'}),
			'post_text' : forms.Textarea(attrs={'class':'form-control'}),
			'post_image' : forms.ClearableFileInput(attrs={'class':'form-control'}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']

		widgets = {
			'body' : forms.Textarea(attrs={'class':'form-control'}),
		}

