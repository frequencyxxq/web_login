from django.urls import path
from .views import Register, Login, Index, LogoutUser, Submitted

urlpatterns = [
    path("", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("index/", Index.as_view(), name="index"),
    path("logout", LogoutUser.as_view(), name="logout"),
    path("submitted/", Submitted.as_view(), name="submitted")
]
