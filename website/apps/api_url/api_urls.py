from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_view import api_views

router = DefaultRouter()
router.register('posts', api_views.PostModelViewSet, basename='posts')
router.register('users', api_views.UserModelViewSet, basename='users')
router.register('comments', api_views.CommentModelViewSet, basename='comments')

urlpatterns = [
	path('', include(router.urls)),
	path('register/', api_views.UserRegister.as_view()),
	path('loginapi/', api_views.UserLogin.as_view()),
	path('logoutapi/', api_views.UserLogout.as_view(), name='logoutapi'),
]
