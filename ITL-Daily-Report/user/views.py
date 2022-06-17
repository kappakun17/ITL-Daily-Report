from django.shortcuts import render
from .models import User, Staff
from .forms import SignInForm, SignUpForm

# Create your views here.

def userSignIn(request):
    form = SignInForm()
    context = {'message':'', 'form':form}


    if request.method != 'POST':
        return render(request, 'user/base.html',context)

    
    email = request.POST['email']
    password = request.POST['password']

    user = User.manager.get_or_none(email = email)
    print(user)
    if user is None:
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request, 'user/base.html',context)

    # パスワード確認
    if user.password != password:
        context['message'] = 'メールアドレスかパスワードが間違っています。'
        return render(request, 'user/base.html', context)

    # ユーザアカウントがアクティビティか
    if user.is_active == False:
        context['message'] = 'スタッフからの承認をお待ちください。'
        return render(request, 'user/base.html', context)

    # ログイン許可
    context['message'] = 'ログインできました。'
    return render(request, 'user/base.html', context)


def userSignUp(request):
    return render(request, 'user/base.html',{})

def staffSignIn(request):
    data = Staff.objects.get(id=1)
    context = {'test': data}
    return render(request, 'user/base.html',context)

def staffSignUp(request):
    return render(request, 'user/base.html', {})