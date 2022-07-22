from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from dialy.models import Dialy
from schedule.models import Schedule
import datetime
from datetime import date
# Create your views here.


class UserDashboard(LoginRequiredMixin,TemplateView):
    
    signin_url = '/signin'

    def __init__(self):
        self.params = {}

    def get(self, request):

        today = datetime.datetime.now()
        lastWeek = datetime.datetime.now() - datetime.timedelta(days=7)
        if not self.request.user.is_staff:
            user_group = self.request.user.user_group.group
            print(user_group)
        
        
            schedules = Schedule.objects.filter(start_time__range=[lastWeek, today], training__group=user_group)

            dialys = []
            for schedule in schedules:

                dialy = Dialy.objects.get_or_none(schedule_id = schedule.id, user_id = self.request.user.id)

                if dialy is not None:

                    dialys.append(
                        {
                            'id':dialy.id,
                            'understandScore':dialy.understandScore,
                            'comment':dialy.comment,
                            'is_public':dialy.is_public,
                            'schedule_id':schedule.id,
                            'date':schedule.start_time.strftime("%Y/%m/%d")
                        }
                        )
       

            self.params['dialys'] = dialys



            todaySchedule = Schedule.objects.get_or_none(
                start_time__year=today.year, 
                start_time__month = today.month,
                start_time__day = today.day,
                training__group=user_group
                )

            

            

            d = today.date()
            year = d.strftime("%Y")
            month = d.strftime("%m")
            monthStr = d.strftime("%B")
            day = d.strftime("%d")

            todayInfo = {
                'year':year,
                'month':monthStr,
                'day':day,
                }

            self.params['today_info'] = todayInfo

            if todaySchedule is None:
                self.params['today_schedule'] = {
                'title':None,
                }

            else:
                self.params['today_schedule'] = {
                    'title':todaySchedule.training.title,
                    'description':todaySchedule.training.description,
                    'staff_memo':todaySchedule.staff_memo,
                    'traineer_memo':todaySchedule.traineer_memo
                    }


        return render(request, 'dashboard/index.html', self.params)

    def post(self,request):
        logout(request)
        redirect(signin_url)

class StaffDashboard(LoginRequiredMixin,TemplateView):
    login_url = '/staff/signin'
    def get(self, request):
        return render(request, 'dashboard/index.html')