from django import forms
from .models import Post, Image, PostComments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

'''ccccccccccccccccccc
class post_from(forms):
    title = forms.CharField(label='title', max_length=40)
    content = forms.CharField(max_length=400)
'''


class Image_Upload(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)


class Image_form(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple":True})
    )

    class Meta:
        model = Image
        fields = ("image",)


class UserCreate(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

'''
class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username')'''


class PostCreate(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ('text',)
