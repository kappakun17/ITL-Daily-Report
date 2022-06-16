from django.shortcuts import render
from user.models import User, Staff

# Create your views here.

def userSignIn(request):
    data = User.objects.get(id=1)
    context = {'test': data}
    return render(request, 'user/base.html',context)

def staffSignIn(request):
    data = Staff.objects.get(id=1)
    context = {'test': data}
    return render(request, 'user/base.html',context)