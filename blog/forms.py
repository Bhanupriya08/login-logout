from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Post,Comment
from django.utils import timezone



class UserLoginForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ('username','email','bio','dob')


class PostForm(forms.ModelForm):
	#author = CustomUser.username

	class Meta:
		model = Post
		fields = ('title', 'text','image')

class Subscribe(forms.Form):
	Email =forms.EmailField()


#to comment on post
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
	
	
		