from django.shortcuts import render

# Create your views here.

def userSignIn(request):
    context = {'test':'welcome to Sign In'}
    return render(request, 'user/base.html',context)