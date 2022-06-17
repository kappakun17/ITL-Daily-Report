from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=250)
    password = forms.CharField(max_length=50)
    

class SignUpForm(forms.Form):
    last_name = forms.CharField(label='姓', max_length=100)
    first_name = forms.CharField(label='名', max_length=100)
    email = forms.EmailField(label='メール',max_length=250)
    re_email = forms.EmailField(label='メール再入力', max_length=250)
    password = forms.CharField(label='パスワード', max_length=50)
    re_password = forms.CharField(label='パスワード再入力', max_length=50)

