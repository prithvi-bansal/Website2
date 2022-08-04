from django.shortcuts import render
from django.views.generic import View,  ListView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import SignUpForm
# from .signals import notification
# Create your views here.

def home(request):
	# notification.send(sender=None, request=request, user=None) #Signal Send
	return render(request, 'users/home.html')

def dashboard(request):
	return render(request, 'users/dashboard.html')

class Signup(CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

class UserEditProfile(UpdateView):
	form_class = UserChangeForm
	success_url = reverse_lazy('userprofile')
	template_name = 'registration/user_editprofile.html'

	def get_object(self):
		return self.request.user

def UserChangePass(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PasswordChangeForm(user=request.user, data=request.POST)
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				messages.success(request, 'Your Password was changed successfully')
				return HttpResponseRedirect('/home/profile/')
		else:
			form = PasswordChangeForm(user=request.user)
		return render(request, 'users/changepass.html', {'form':form})
	else:
		return HttpResponseRedirect('/login/')

class Profile(ListView):
	model = Profile
	template_name = 'registration/user_profile.html'
