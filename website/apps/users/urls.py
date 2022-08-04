from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('signup/', views.Signup.as_view(), name='signup'),
	path('profile/', views.Profile.as_view(), name='userprofile'),
	path('editprofile/', views.UserEditProfile.as_view(), name='usereditprofile'),
	path('changepass/', views.UserChangePass, name='changepass'),

]