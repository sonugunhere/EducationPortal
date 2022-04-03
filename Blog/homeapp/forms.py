from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Create your forms here.
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


# class ProfileForm(UserCreationForm):
# 	username = forms.CharField(max_length=200)
# 	email = forms.EmailField(required=True)
	
# 	class Meta:
# 		model = Profile
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(ProfileForm, self).save(commit=True)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user