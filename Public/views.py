# Create your views here.

from .models import Meetings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def home(request):
    upcomingMeetings = Meetings.objects.order_by("-date")[:3]
    context = {"upcomingMeetings":upcomingMeetings}
    return render(request, "home.html", context)

def signUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully.")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Please fix the errors above.")
    else:
        form = UserCreationForm()

    return render(request, "signUp.html", {"form": form})

def loginView(request):
    return render(request, "login.html")

def settings(request):
    return render(request, "settings.html")

def viewBooking(request):
    return render(request, "viewBooking.html")

def book(request):
    return render(request, "book.html")

def editBooking(request, meetingID):
    meeting = get_object_or_404(Meetings, pk=meetingID)
    return render(request, "editBooking.html", {"meeting":meeting})
