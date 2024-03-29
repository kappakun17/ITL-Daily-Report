from django import forms



class SignInForm(forms.Form):
    email = forms.EmailField(label='メールアドレス',max_length=250)
    password = forms.CharField(label='パスワード',max_length=50)
    

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='名 (英字)', max_length=100)
    last_name = forms.CharField(label='姓 (英字)', max_length=100)
    email = forms.EmailField(label='メールアドレス',max_length=250)
    re_email = forms.EmailField(label='メールアドレス再入力', max_length=250)
    password = forms.CharField(label='パスワード', max_length=50)
    re_password = forms.CharField(label='パスワード再入力', max_length=50)

