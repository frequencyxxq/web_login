from django.shortcuts import render, reverse, redirect

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Organization, Room, IssueCategory, IssueSubcategory, Ticket


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
        context = {}
        organizations = Organization.objects.all()
        rooms = Room.objects.all()

        categories = {}
        issue_categories = IssueCategory.objects.all()
        for issue_category in issue_categories:
            issue_subcategories = IssueSubcategory.objects.filter(
                issue_categoty=issue_category
            )
            categories[issue_category.content] = issue_subcategories

        context["organizations"] = organizations
        context["rooms"] = rooms
        context["categories"] = categories

        return render(request, "index.html", context=context)

    def post(self, request):
        organization_id = request.POST.get("organization", "")
        number = request.POST.get("number", "")
        reporter = request.POST.get("reporter", "")
        telnumber = request.POST.get("telnumber", "")
        issue_subcategory_id = request.POST.get("issue_subcategory", "")
        description = request.POST.get("description", "")

        issue_subcategory = IssueSubcategory.objects.get(id=issue_subcategory_id)
        organization = Organization.objects.get(id=organization_id)
        room = Room.objects.get(id=number)

        ticket = Ticket.objects.create(
            user=request.user,
            reporter=reporter,
            solved_by="",
            mobile_phone=telnumber,
            remark=description,
            issue_category=issue_subcategory.issue_categoty,
            issue_subcategory=issue_subcategory,
            organization=organization,
            room=room,
        )

        print(ticket)
        return redirect(reverse("submitted"))


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("register"))

    def post(self, request):
        pass


class Submitted(View):
    def get(self, request):
        return render(request, "submitted.html")

    def post(self, request):
        pass
