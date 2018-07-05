from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
    )

from .models import OurGallery,Testimonial,Blog,FreeCounselling,PhotoGallery,MediaGallery

User = get_user_model()



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        user1 = self.cleaned_data.get("username")
        pass1 = self.cleaned_data.get("password")
        if user1 and pass1:

            user = authenticate(username=user1, password=pass1)
            if not user:
                raise forms.ValidationError("Invalid Username or password")
            if not user.check_password(pass1):
                raise forms.ValidationError("Invalid Password")

            if not user.is_active:
                raise forms.ValidationError("No longer active")


        return super(UserLoginForm, self).clean(*args, **kwargs)


class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields=[
            "comment","name","occupation",
        ]

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[
           "title", "para1","image","para2"
        ]

class FreeCounsellingForm(forms.ModelForm):
    class Meta:
        model=FreeCounselling
        fields= [
            "name", "email", "mobile"
        ]

class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model=PhotoGallery
        fields = [
            "desc","image"
        ]

class MediaGalleryForm(forms.ModelForm):
    class Meta:
        model=MediaGallery
        fields=[
            "title","desc","image"
        ]