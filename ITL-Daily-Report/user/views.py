from django.shortcuts import render
from .models import User, Staff
from .forms import SignInForm, SignUpForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

userView = {
    'signIn':'user/user_sign_in.html',
    'signUp':'user/user_sign_up.html'
    }
staffView = {
    'signIn':'user/staff_sign_in.html',
    'signUp':'user/staff_sign_up.html'
    }
allView = {
    'pleaseWait':'user/please_wait.html'
    }

def userSignIn(request):
    global userView

    form = SignInForm()
    context = {'message':'', 'form':form}


    if request.method != 'POST':
        return render(request, userView['signIn'] ,context)

    
    email = request.POST['email']
    password = request.POST['password']

    user = User.manager.get_or_none(email = email)
    
    # アカウント有無の確認

    if user is None:
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request, userView['signIn'],context)

    # パスワード確認
    if not check_password(password, user.password):
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request, userView['signIn'], context)

    # ユーザアカウントがアクティビティか
    if user.is_active == False:
        context['message'] = 'スタッフからの承認をお待ちください。'
        return render(request, userView['signIn'], context)

    # ログイン許可
    #context['message'] = 'ログインできました。'
    return render(request,allView['pleaseWait'], context)


def userSignUp(request):
    form = SignUpForm(request.POST or None)
    context = {'message':'', 'form':form}
    
    if request.method != 'POST':
        return render(request,userView['signUp'], context)
    if not form.is_valid():
        context['message'] = 'フォームに入力間違いがあります'
        return render(request, userView['signUp'], context)

    email = form.cleaned_data['email']
    re_email = form.cleaned_data['re_email']
    password = form.cleaned_data['password']
    re_password = form.cleaned_data['re_password']

    if email != re_email:
        context['message'] = 'メールアドレスが一致しません'
        return render(request, userView['signUp'], context)

    if password != re_password:
        context['message'] = 'パスワードが一致しません'
        return render(request, userView['signUp'], context)

    if User.manager.get_or_none(email = email):
        context['message'] = 'すでに登録されているメールアドレスです'
        return render(request, userView['signUp'], context)

    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['first_name']

    data = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password),
        )

    data.save()
    context['message'] = '保存しました'
    return render(request, allView['pleaseWait'], context)


def staffSignIn(request):
    form = SignInForm()
    context = {'message':'', 'form':form}


    if request.method != 'POST':
        return render(request, staffView['signIn'],context)

    
    email = request.POST['email']
    password = request.POST['password']

    staff = Staff.manager.get_or_none(email = email)
   
    # アカウント有無の確認
    if staff is None:
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request,staffView['signIn'],context)

    # パスワード確認
    if not check_password(password, staff.password):
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request, staffView['signIn'], context)

    # ユーザアカウントがアクティビティか
    if staff.is_active == False:
        context['message'] = 'スタッフからの承認をお待ちください。'
        return render(request, allView['pleaseWait'], context)

    # ログイン許可
    context['message'] = 'ログインできました。'
    return render(request, allView['pleaseWait'], context)

def staffSignUp(request):

    form = SignUpForm(request.POST or None)
    context = {'message':'', 'form':form}
    
    if request.method != 'POST':
        return render(request, staffView['signUp'], context)
    
    if not form.is_valid():
        context['message'] = 'フォームに入力間違いがあります'
        return render(request, staffView['signUp'], context)

    email = form.cleaned_data['email']
    re_email = form.cleaned_data['re_email']
    password = form.cleaned_data['password']
    re_password = form.cleaned_data['re_password']

    if email != re_email:
        context['message'] = 'メールアドレスが一致しません'
        return render(request, 'user/base.html', context)

    if password != re_password:
        context['message'] = 'パスワードが一致しません'
        return render(request, staffView['signUp'], context)

    if Staff.manager.get_or_none(email = email):
        context['message'] = 'すでに登録されているメールアドレスです'
        return render(request, staffView['signUp'], context)

    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['first_name']

    data = Staff(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password),
        )

    data.save()
    context['message'] = '保存しました'
    return render(request, allView['pleaseWait'], context)




        