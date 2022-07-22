from django import forms


class UserDialyDetailForm(forms.Form):
    detail_id = forms.IntegerField()

class UserDialyEditIdForm(forms.Form):
    edit_id = forms.IntegerField()

class UserDialyEditForm(forms.Form):
    understandScore = forms.IntegerField(max_value=100, min_value=0)
    comment = forms.CharField(max_length=800)
    is_public = forms.CharField(max_length=10) # 文字列のfalse or true

class PostCommentForm(forms.Form):
    dialy_id = forms.IntegerField()
    message = forms.CharField(max_length=300)