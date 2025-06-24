from django.urls import path

from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("index/", views.index, name="index"),
    path("home/", views.home, name = "home"),
    path("signUp/", views.signUp, name = "signUp"),
    path("login/", views.loginView, name = "login"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
    path("settings/", views.settings, name = "settings"),
    path("viewBooking/", views.viewBooking, name = "viewBooking"),
    path("editBooking/<int:meetingID>", views.editBooking, name = "editBooking"),
    path("book/", views.book, name = "book"),
]