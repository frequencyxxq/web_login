from django.shortcuts import render, reverse, redirect

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("index"))

        return render(request, "register.html")

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        check_password = request.POST.get("check_password", "")

        if password != check_password:
            return HttpResponse("密码输入不一致")

        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse("该账号已注册")
        User.objects.create_user(username=username, password=password)

        return redirect(reverse("login"))


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse("该账号不存在")
        user = authenticate(username=username, password=password)  # 自动验证
        if user:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return HttpResponse("密码错误")


class Index(View):
    def get(self, request):

        return render(request, "index.html")

    def post(self, request):
        organization = request.POST.get("organization", "")
        number = request.POST.get("number", "")
        reporter = request.POST.get("reporter", "")
        telnumber = request.POST.get("telnumber", "")
        classification = request.POST.get("classification", "")
        classification2 = request.POST.get("classification2", "")
        description = request.POST.get("description", "")
        print(organization, number, reporter, telnumber, classification, classification2, description)
        return redirect(reverse("index"))

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("register"))

    def post(self, request):
        pass
