from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from posts.models import Post, Comment
from posts.serializers import PostSerializer, PostSerializer2, UserSerializer, UserRegisterSerializer, UserLoginSerializer, CommentSerializer
from posts.permissions import IsAuthorOrReadOnly


class PostList(APIView):
	# permission_classes = (IsAuthenticatedOrReadOnly,)

	def get(self, request, format=None):
		post = Post.objects.all()
		serializer = PostSerializer(post, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PostSerializer2(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
	def get(self, request, format=None):
		pk = self.request.GET['pk']
		post = Post.objects.get(id=pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def put(self, request, format=None):
		pk = self.request.GET['pk']
		post = Post.objects.get(id=pk)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		pk = self.request.GET['pk']
		post = Post.objects.get(id=pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostModelViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('id')
	serializer_class = PostSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class CommentModelViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class UserModelViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserRegister(generics.GenericAPIView):
	serializer_class = UserRegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			# send_mail(
			# 	'Account Created',
			# 	'Your Account was Created Successfully'
			# 	'Login Here'
			# 	'http://127.0.0.1:8080/login/',
			# 	settings.EMAIL_HOST_USER,
			# 	[user.email]
			# 	)
			msg = EmailMessage(
					'Account Created',
					'Your Account was Created Successfully<br>'
					'Login Here<br>'
					'http://127.0.0.1:8080/login/',
					settings.EMAIL_HOST_USER,
					[user.email]
				)
			msg.content_subtype = "html"
			msg.send()
			return Response(serializer.data)
		return Response(serializer.errors)

class UserLogin(generics.GenericAPIView):
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			username = serializer.data.get('username')
			password = serializer.data.get('password')
			user = authenticate(username=username, password=password)
			if not user:
				return Response({'error': 'Invalid Credentials'})
			login(request, user)
			token = Token.objects.get_or_create(user=user)
			token = token[0].key
			return Response({'user':serializer.data, 'token':token})
		return Response(serializer.errors)

class UserLogout(generics.GenericAPIView):
	def get(self, request, *args, **kwargs):
		user = request.user
		token = Token.objects.filter(user=user)
		token.delete()
		logout(request)
		return Response({'msg':'Logged Out Successfully'})

