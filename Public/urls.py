from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name = "home"),
    path("signUp/", views.signUp, name = "signUp"),
    path("login/", views.login, name = "login"),
    path("settings/", views.settings, name = "settings"),
    path("viewBooking/", views.viewBooking, name = "viewBooking"),
    path("editBooking/<int:meetingID>", views.editBooking, name = "editBooking"),
    path("book/", views.book, name = "book"),
]