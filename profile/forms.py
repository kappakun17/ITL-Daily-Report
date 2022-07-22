from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['hobby', 'introduction', 'user_image']

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_image']

class UserProfileAllForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'