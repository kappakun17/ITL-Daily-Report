from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AccountManagement(TemplateView):
    
    def get(self,request):
        return render(request, 'accountManagement/index.html')