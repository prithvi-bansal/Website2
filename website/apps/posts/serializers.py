from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source = 'author.username')
	class Meta:
		model = Comment
		fields = ['id', 'author', 'body', 'post']

class PostSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source = 'author.username')
	comments = CommentSerializer(many=True)
	class Meta:
		model = Post
		fields = ['id', 'post_title', 'author', 'post_text', 'post_image', 'likes_count', 'comments']

class UserSerializer(serializers.ModelSerializer):
	posts = PostSerializer(many=True)
	
	class Meta:
		model = User
		fields = ['id', 'username', 'posts']

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(style={'input_type':'password'})

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
		return user
