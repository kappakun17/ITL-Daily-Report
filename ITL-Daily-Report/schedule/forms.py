from django import forms


class ScheduleForm(forms.Form):
    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)


