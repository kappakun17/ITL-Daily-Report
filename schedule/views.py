from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.views.generic import TemplateView
from .models import Schedule
from dialy.models import Dialy
from .forms import ScheduleForm
import json
import time
# Create your views here.


class UserSchedule(LoginRequiredMixin ,TemplateView):

    def __init__(self):

        self.params = {}

    def get(self, request):
        get_token(request)
        return render(request, 'schedule/staff_schedule.html', self.params)


class GetEvents(LoginRequiredMixin,TemplateView):

    def get(self, request):

        raise Http404()


    def post(self, request):

        datas = json.loads(request.body)

        form = ScheduleForm(datas)
        if form.is_valid() == False:
            raise Http404

        start_date = datas['start_date']
        end_date = datas['end_date']

        formatted_start_date = time.strftime(
            "%Y-%m-%d", time.localtime(start_date / 1000))

        formatted_end_date = time.strftime(
            "%Y-%m-%d", time.localtime(end_date / 1000))

        events = Schedule.objects.filter(
            start_time__lt=formatted_end_date, end_time__gt=formatted_start_date, training__group=self.request.user.user_group.group).order_by('start_time')

        list = []
        for event in events:
            
            is_dialy = False
            dialy_data = Dialy.objects.get_or_none(schedule_id = event, user_id=self.request.user)
            print(dialy_data)
            if dialy_data is not None:
                is_dialy = True     
            
            print(is_dialy)
            list.append(
                {
                 'id':event.id,
                 'title':event.training.title,
                 'start':event.start_time,
                 'end':event.end_time,
                 'description':event.training.description,
                 'staff_memo':event.staff_memo,
                 'traineer_memo':event.traineer_memo,
                 'is_dialy': is_dialy,
                }
            )

        print(list)
        return JsonResponse(list, safe=False)