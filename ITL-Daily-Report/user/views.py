from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import User
from .forms import SignInForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView 
from django.contrib import messages
from urllib.parse import urlencode

import time


# Create your views here.

userView = {
    'signIn':'user/user_sign_in.html',
    'signUp':'user/user_sign_up.html',
    'confirm':'user/confirm.html',
    'success':'user/success.html',

    }
staffView = {
    'signIn':'user/staff_sign_in.html',
    'signUp':'user/staff_sign_up.html',
    'confirm':'user/confirm.html',
    'success':'user/success.html'
    }
allView = {
    'pleaseWait':'user/please_wait.html'
    }

class UserSignIn(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignInForm()
            }

    def get(self, request):
        
        if self.request.user.is_authenticated:
            user = self.request.user
            return redirect('/dashboard/user')

        return render(request, userView['signIn'], self.params)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        if email == '' and password == '':
            self.params['message'] = 'アカウントと、パスワードを入力してください。'
            return render(request, userView['signIn'], self.params)



        is_user = User.objects.get_or_none(email=email)

        print(is_user)

        if not is_user:
            self.params['message'] = 'メールアドレス化パスワードが間違っています。'
            return render(request, userView['signIn'], self.params)

        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            if not user.is_activated:
                return redirect('/please-wait')
            return redirect('/dashboard/user')
        else:
            self.params['message'] = 'メールアドレスかパスワードが間違っています。'
            return render(request, userView['signIn'], self.params)


class SignoutView(LoginRequiredMixin, LogoutView):
    template_name = userView['signIn']

class UserSignUp(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self,request):

        if request.session:
            self.params['form'] = SignUpForm(request.session.get('sign-up'))
            return render(request, userView['signUp'], self.params)
        else:
            return render(request, userView['signUp'], self.params)

    def post(self, request):
        self.params['form'] = SignUpForm(request.POST)

        if not self.params['form'].is_valid():
            self.params['message'] = 'フォーム入力に誤りがあります'
            return render(request,userView['signUp'], self.params)

        form = self.params['form']

        # チェック後のデータを各変数に格納
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        re_email = form.cleaned_data['re_email']
        password = form.cleaned_data['password']
        re_password = form.cleaned_data['re_password']

        # 入力データの条件チェック
        # 1.メールアドレスの一致
        # 2.パスワードの一致
        # 3.メールアドレスがすでに登録されているかどうかの確認

        # 1
        if email != re_email:
            self.params['message']='メールアドレスが一致しません'
            return render(request,userView['signUp'],self.params)

        # 2
        if password != re_password:
            self.params['message'] = 'パスワードが一致しません'
            return render(request, userView['signUp'], self.params)

        # 3
        if User.objects.get_or_none(email = email):
            self.params['message'] = 'すでに登録されているメールアドレスです'
            return render(request, userView['signUp'], self.params)

        # バリデーションチェックしたデータをセッションにしまう
        # リダイレクトで、confirmに飛ばす
        request.session['sign-up'] = request.POST
        return redirect('/signup/confirm')



class StaffSignIn(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignInForm()
            }

    def get(self, request):
        
        if self.request.user.is_authenticated and self.request.user.is_staff:
            user = self.request.user
            return redirect('/dashboard/staff')

        return render(request, staffView['signIn'], self.params)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email = email, password = password)
        if user is not None:
            if not user.is_staff:
                self.params['message'] = 'スタッフ認証が必要です。管理者にお問い合わせください。'
                return render(request, staffView['signIn'],self.params)
            
            login(request, user)
            if not user.is_activated:
                return redirect('/please-wait')
           
            return redirect('/dashboard/user')
        
        else:
            self.params['message'] = 'メールアドレスかパスワードが間違っています。'
            return render(request, userView['signIn'], self.params)

class StaffSignUp(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self,request):

        if request.session:
            self.params['form'] = SignUpForm(request.session.get('staff-sign-up'))
            return render(request, staffView['signUp'], self.params)
        else:
            return render(request, staffView['signUp'], self.params)

    def post(self, request):
        self.params['form'] = SignUpForm(request.POST)

        if not self.params['form'].is_valid():
            self.params['message'] = 'フォーム入力に誤りがあります'
            return render(request,staffView['signUp'], self.params)

        form = self.params['form']

        # チェック後のデータを各変数に格納
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        re_email = form.cleaned_data['re_email']
        password = form.cleaned_data['password']
        re_password = form.cleaned_data['re_password']

        # 入力データの条件チェック
        # 1.メールアドレスの一致
        # 2.パスワードの一致
        # 3.メールアドレスがすでに登録されているかどうかの確認

        # 1
        if email != re_email:
            self.params['message']='メールアドレスが一致しません'
            return render(request,staffView['signUp'],self.params)

        # 2
        if password != re_password:
            self.params['message'] = 'パスワードが一致しません'
            return render(request, staffView['signUp'], self.params)

        # 3
        if User.objects.get_or_none(email = email):
            self.params['message'] = 'すでに登録されているメールアドレスです'
            return render(request, staffView['signUp'], self.params)

        # バリデーションチェックしたデータをセッションにしまう
        # リダイレクトで、confirmに飛ばす
        request.session['staff-sign-up'] = request.POST
        return redirect('/staff/signup/confirm')




class UserConfirm(TemplateView):
    
    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self,request):

        if request.session:
            data = request.session.get('sign-up')
            form = SignUpForm(data or None)
            if not form.is_valid():
                return render(request, userView['signUp'], self.params)
            confirmData = {}
            confirmData['first_name'] = form.cleaned_data['first_name']
            confirmData['last_name'] = form.cleaned_data['last_name']
            confirmData['email'] = form.cleaned_data['email']
            confirmData['password'] = form.cleaned_data['password']

            self.params['confirm_data'] = confirmData  
            return render(request, userView['confirm'], self.params)
  
    def post(self, request):
        if request.session:
            data = request.session.get('sign-up')
            request.session.clear()

            self.params['form'] = SignUpForm(data)
            form = self.params['form']
            form.is_valid()

            # 登録データの取得
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Userデータベースへ登録
            db = User.objects.create_user(first_name, last_name, email, password)
            db.save()

            ## 自動ログイン
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print(user)
                login(request, user)
            else:
                print(user)
                return redirect('/')

            print(self.request.user)

            request.session['is-sign-up'] = True

            return redirect('/signup/success')

    
class StaffConfirm(TemplateView):
    
    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self,request):

        if request.session:
            data = request.session.get('staff-sign-up')
            form = SignUpForm(data or None)
            if not form.is_valid():
                return render(request, staffView['signUp'], self.params)
            confirmData = {}
            confirmData['first_name'] = form.cleaned_data['first_name']
            confirmData['last_name'] = form.cleaned_data['last_name']
            confirmData['email'] = form.cleaned_data['email']
            confirmData['password'] = form.cleaned_data['password']

            self.params['confirm_data'] = confirmData  
            return render(request, staffView['confirm'], self.params)
  
    def post(self, request):
        if request.session:
            data = request.session.get('staff-sign-up')
            request.session.clear()

            self.params['form'] = SignUpForm(data)
            form = self.params['form']
            form.is_valid()

            # 登録データの取得
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Userデータベースへ登録
            db = User.objects.create_staff(first_name, last_name, email, password)
            db.is_staff = True
            db.save()

            ## 自動ログイン, 
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print(user)
                login(request, user)
            else:
                print(user)
                return redirect('/')

            print(self.request.user)

            request.session['is-staff-sign-up'] = True

            return redirect('/staff/signup/success')

class UserSuccess(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self, request):
        if request.session:
            if request.session.get('is-sign-up') and self.request.user:
                print(self.request.user)
                user = User.objects.get_or_none(id=self.request.user.id)
                return render(request, 'user/success.html', {'user':user})

        else:
            return redirect('/signup')
                
    def post(self, request):
        return redirect('/initial-profile/user')

class StaffSuccess(TemplateView):

    def __init__(self):
        self.params = {
            'message':'',
            'form':SignUpForm(),
            }

    def get(self, request):
        if request.session:
            if request.session.get('is-staff-sign-up') and self.request.user:
                user = User.objects.get_or_none(id=self.request.user.id)
                return render(request, 'user/success.html', {'user':user})

        else:
            return redirect('/staff/signup')
                
    def post(self, request):
        return redirect('/initial-profile/staff')

class pleaseWait(TemplateView):
    def __init__(self):
        self.params = {}

    def get(self,request):

        if not request.user.is_authenticated:
            return redirect('/')

        user = self.request.user
        logout(request)

        return render(request, allView['pleaseWait'],{'user':user})
    
    def post(self,request):

        if request.method != 'POST':
            return redirect('/signin')