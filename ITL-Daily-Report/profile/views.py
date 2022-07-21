from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserProfileForm
from .models import Profile
from user.models import User
from django.http import Http404

# Create your views here.

default_user_image = '/'

class UserInitialProfile(TemplateView):
    
    def __init__(self):
        self.params = {
            'message':'',
            'form':UserProfileForm()
            }

    def get(self,request):

        if self.request.user:
            user = self.request.user
            return render(request, 'profile/initial_profile.html', self.params)
        else:
            return Http404('必要なデータがありません')

    def post(self, request):

        self.params['form'] = UserProfileForm(request.POST,request.FILES,instance=request.user)
        form = self.params['form']

        if not form.is_valid():
            self.params['message'] = '入力データに誤りがあります。'
            return render(request, 'profile/initial_profile.html', self.params)

        if 'user_image' in request.FILES:
            user_image = request.FILES['user_image']
        else:
            user_image = 'profile_images/default/user.png'

        hobby = form.cleaned_data['hobby']
        introduction = form.cleaned_data['introduction']


        print(hobby)
        print(introduction)
        print(user_image)
        user = self.request.user
        db = Profile(
            user_id = user.id,
            hobby=hobby,
            introduction = introduction,
            user_image = user_image,
            )
        db.save()

        return redirect('/please-wait')

class StaffInitialProfile(TemplateView):
    
    def __init__(self):
        self.params = {
            'message':'',
            'form':UserProfileForm()
            }

    def get(self,request):

        if self.request.user:
            user = self.request.user
            return render(request, 'profile/initial_profile.html', self.params)
        else:
            return Http404('必要なデータがありません')

    def post(self, request):

        self.params['form'] = UserProfileForm(request.POST,request.FILES,instance=request.user)
        form = self.params['form']

        if not form.is_valid():
            self.params['message'] = '入力データに誤りがあります。'
            return render(request, 'profile/initial_profile.html', self.params)

        if 'user_image' in request.FILES:
            user_image = request.FILES['user_image']
        else:
            user_image = 'profile_images/default/user.png'

        hobby = form.cleaned_data['hobby']
        introduction = form.cleaned_data['introduction']


        print(hobby)
        print(introduction)
        print(user_image)
        user = self.request.user
        db = Profile(
            user_id = user.id,
            hobby=hobby,
            introduction = introduction,
            user_image = user_image,
            )
        db.save()

        return redirect('/please-wait')

    
class ProfileView(TemplateView):

    def get(self, request):

        return render(request, 'profile/profile_view.html')