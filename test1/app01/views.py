from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django .contrib.auth.decorators import login_required
from app01 import models
from app01.models import UserInfo
from app01.utils.encrypt import md5
from app01.utils.bootstrap import BootStrapForm
# Create your views here.


class LoginForm(BootStrapForm):  # 登入欄位
    email = forms.CharField(
        label="E-mail",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):  # 登入
    ##### 登入 #####
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():

        # 成功拿到值 {'name':'test123', 'password': '123'}
        print(form.cleaned_data)

        # 到資料庫比對資料(**以字典型態)
        # 登入頁面所填的資料
        user_object = UserInfo.objects.filter(**form.cleaned_data).first()

        if not user_object:  # 比對失敗
            form.add_error("password", "名稱或密碼錯誤")  # 在password下方顯示錯誤訊息
            return render(request, 'login.html', {'form': form})

        # 比對成功
        # 在 cookie 和 session 加入字串
        request.session['info'] = {
            'id': user_object.id, 'name': user_object.name}
        return redirect("/teaching/")

    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect("/")


CHOICES = [('1', '男性'),
           ('2', '女性')]


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["email", "name", "password", "bithday", "sex", "Depart"]

        widgets = {  # 樣式設定
            "password": forms.PasswordInput(render_value=True),
            "bithday": forms.DateInput(attrs={'type': 'date'}),
            "sex": forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-input'}),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def singup(request):  # 註冊
 ##### ModelForm方式增加使用者 #####

    if request.method == 'GET':

        form = UserModelForm()
        return render(request, 'singup.html', {"form": form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'singup.html', {"form": form})


def exercise(req):
    return render(req, "exercise.html")


def teaching(req):
    return render(req, "teaching.html")
