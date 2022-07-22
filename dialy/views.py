from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserDialyDetailForm, UserDialyEditIdForm, UserDialyEditForm, PostCommentForm
from .models import Dialy, Message
from profile.models import Profile
from schedule.models import Schedule
from accountManagement.models import ITLGroupUser
from user.models import User
from datetime import datetime, timedelta
import calendar
import locale
import json


# Create your views here.

class UserDialy(LoginRequiredMixin, TemplateView):

    def __init__(self):
        self.params = {}
    def get(self, request):


        today = datetime.today()
        today_year = today.year
        today_month = today.month

        

        dialys = Dialy.objects.filter(
            schedule_id__start_time__year = today_year, 
            schedule_id__start_time__month = today_month, 
            user_id = self.request.user.id).order_by('schedule_id__start_time')

        print(dialys)

        user_dialys = []

        monthRange = calendar.monthrange(today_year, today_month)[1]

        # get the date list
        date_list = [datetime(today_year, today_month,1) + timedelta(days=i) for i in range(monthRange)]

        date_str_list = [d.strftime('%m/%d') for d in date_list]

        for i in range(len(date_str_list)):

            if dialys:
                for j in range(len(dialys)):
                    date = dialys[j].schedule_id.start_time
                    str_date = date.strftime('%m/%d')
        
                    if str_date == date_str_list[i]:

                        user_dialys.append({
                            'id':dialys[j].id,
                            'schedule_id':dialys[j].schedule_id.id,
                            'date':date_str_list[i],
                            'year':date.strftime('%Y'),
                            'day':date_list[i].strftime('%A'),
                            'training_title':dialys[j].schedule_id.training.title,
                            'comment':dialys[j].comment,
                            'understandScore':dialys[j].understandScore,
                
                            })

                  

                if len(user_dialys) != i+1:
                    user_dialys.append({
                    'date':date_str_list[i],
                    'day':date_list[i].strftime('%A'),
                    'training_title':''
                        })
                    print(str_date + '==' + date_str_list[i])



            else:
                user_dialys.append({
                'date':date_str_list[i],
                'day':date_list[i].strftime('%A'),
                'training_title':''
                    })
                   
                
        
        print(user_dialys)
            

        self.params['dialys'] = user_dialys

        return render(request, 'dialy/dialy_views.html', self.params)








class UserDialyDetail(LoginRequiredMixin,TemplateView):
    
    def __init__(self):
        self.params = {}

    def get(self, request, detail_id):
       
       initial_dict = dict(detail_id=detail_id)
       form = UserDialyDetailForm(initial_dict)
       
       if form.is_valid() == False:
           return Http404()


       if self.request.user.user_group is None:
           return (request, 'dialy/cantAccess.html')

       schedule_data = Schedule.objects.get_or_none(id=detail_id, training__group = self.request.user.user_group.group)
       

       schedule_date = {}

       locale.setlocale(locale.LC_CTYPE, "Japanese_Japan.932")
       schedule_date['str_date'] = schedule_data.start_time.strftime('%Y年%m月%d日')
       schedule_date['str_start'] = schedule_data.start_time.strftime('%H:%M')
       schedule_date['str_end'] = schedule_data.end_time.strftime('%H:%M')

       self.params['schedule'] = schedule_data
       self.params['schedule_date'] = schedule_date

       dialys = Dialy.objects.filter(schedule_id=schedule_data.id, schedule_id__training__group = self.request.user.user_group.group)

       print(dialys)
       user_dialy = {}
       user_message = []
       other_dialys = []



       for dialy in dialys:
           if dialy.user_id.id == self.request.user.id:
               user_dialy['id'] = dialy.id
               user_dialy['understandScore'] = dialy.understandScore
               user_dialy['comment'] = dialy.comment
               user_dialy['is_public'] = dialy.is_public

               user_messages = Message.objects.filter(dialy=dialy.id)
               user_message_list = []

               if user_messages:
                   for message in user_messages:

                       user_profile = Profile.objects.get(user=message.user.id)
                       user_message_list.append({
                           'id':message.id,
                           'user_name':message.user,
                           'user_group':message.user.user_group.group,
                           'user_image':user_profile.user_image,
                           'message':message.message,
                           'send_time':message.send_time,
                           })
            
           else:
               if dialy.is_public:
                   user_profile = Profile.objects.get(user = dialy.user_id)

                   other_dialys.append(
                       {
                       'id':dialy.id,
                       'understandScore': dialy.understandScore,
                       'comment':dialy.comment,
                       'is_public':dialy.is_public,
                       'user_name':dialy.user_id,
                       'user_group':self.request.user.user_group.group,
                       'user_image':user_profile.user_image,
                       }
                   )
                   
                   other_messages = Message.objects.filter(dialy=dialy.id)

                   other_message_list = []

                   if other_messages:
                       for comment in other_messages:

                           user_profile = Profile.objects.get(user=comment.user.id)
                           other_message_list.append({
                               'id':comment.id,
                               'user_name':comment.user,
                               'user_group':comment.user.user_group.group,
                               'user_image':user_profile.user_image,
                               'message':comment.message,
                               'send_time':comment.send_time,
                               })
                       print(other_message_list)
                       other_dialys[len(other_dialys)-1]['other_messages'] = other_message_list
                       other_dialys[len(other_dialys)-1]['messages_count'] = str(len(other_message_list))

       print(other_dialys)
       self.params['user_messages'] = user_message_list
       print(user_message_list)
       self.params['user_dialy'] = user_dialy
       self.params['other_dialys'] = other_dialys
       

       if schedule_data is None:
           return Http404()

       user = User.objects.get_or_none(id=self.request.user.id)
       user_group = user.user_group.group
       print(schedule_data.training.group, user_group)
       if schedule_data.training.group != user_group:
           return Http404()

       return render(request, 'dialy/dialy_detail.html', self.params)


class UserDialyEdit(LoginRequiredMixin, TemplateView):

    def __init__(self):
        self.params = {
            'form':UserDialyEditForm(),
            'message':''
            }

    def get(self, request, edit_id):

        initial_dict = dict(edit_id = edit_id)
        check_form = UserDialyEditIdForm(initial_dict)

        if check_form.is_valid() == False:
            return Http404()

        schedule_data = Schedule.objects.get_or_none(id=edit_id)
        self.params['schedule'] = schedule_data

        if schedule_data is None:
            return Http404()

        dialy_data = Dialy.objects.get_or_none(schedule_id=schedule_data.id, user_id = self.request.user.id)
        print(dialy_data)
        if dialy_data is None:
            self.params['data'] = {
                'understandScore':50,
                'comment':'',
                'is_public':'false',
                }
            self.params['button'] = '登録'
            return render(request, 'dialy/index.html', self.params)
        
        else:
            self.params['data'] = {
                'understandScore':dialy_data.understandScore,
                'comment':dialy_data.comment,
                'is_public':'false' if dialy_data.is_public == 'false' else 'true'
                }
            self.params['message'] = '以前登録された日報です。上書き保存するには、データを修正後、修正完了ボタンをクリックしてください。'
            self.params['button'] = '修正完了'
            return render(request, 'dialy/index.html', self.params)
 


    def post(self, request, edit_id):
        
        form = UserDialyEditForm(request.POST)

        
        if not form.is_valid():
            return Http404()

        if Dialy.objects.get_or_none(schedule_id=edit_id, user_id=self.request.user.id) is None:
            db = Dialy()
        else:
            db = Dialy.objects.get_or_none(schedule_id=edit_id, user_id=self.request.user.id)

        db.schedule_id = Schedule.objects.get_or_none(id=edit_id)
        db.user_id = self.request.user
        db.understandScore = request.POST['understandScore']
        db.comment = request.POST['comment']
        db.is_public = False if request.POST['is_public'] == 'false' else True

        db.save()

        if 'next' in request.GET:
            return redirect(request.GET['next'])
        else:
            return redirect('/dashboard/user/schedule')

class UserDialyPostMessage(LoginRequiredMixin,TemplateView):

    def post(self, request):
        data = json.loads(request.body)

        form = PostCommentForm(data)

        if not form.is_valid():
            return Http404()

        dialy_id = form.cleaned_data['dialy_id']
        message = form.cleaned_data['message']

        print('通りました')

        dialy = Dialy.objects.get_or_none(id=dialy_id)

        newMessage = Message()
        newMessage.user_id = self.request.user.id
        newMessage.dialy_id = dialy.id
        newMessage.message = message
        newMessage.save()

        print(newMessage)

        return JsonResponse(None, safe=False)

            