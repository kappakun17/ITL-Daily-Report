from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.


class UserDashboard(LoginRequiredMixin,TemplateView):
    
    signin_url = '/signin'

    def get(self, request):
        return render(request, 'dashboard/index.html')

    def post(self,request):
        logout(request)
        redirect(signin_url)

class StaffDashboard(LoginRequiredMixin,TemplateView):
    login_url = '/staff/signin'
    def get(self, request):
        return render(request, 'dashboard/index.html')