# Create your views here.

from .models import Meetings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware
from datetime import datetime

def index(request):
    return render(request, "index.html")

@login_required
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
    if request.method == "POST":
        username = request.POST.get("usernameLogin")
        password = request.POST.get("passwordLogin")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

@login_required
def settings(request):
    return render(request, "settings.html")

@login_required
def viewBooking(request):
    return render(request, "viewBooking.html")

@login_required
def book(request):
    if request.method == "POST":
        datetime_str = request.POST.get("bookingDate")
        room = request.POST.get("roomSelection")

        if not datetime_str or not room:
            messages.error(request, "All fields are required.")
            return redirect("viewBooking")

        try:
            dt = make_aware(datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M"))
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect("viewBooking")

        Meetings.objects.create(
            date=dt,
            room=int(room),
            userID=request.user 
        )
        messages.success(request, "Meeting booked successfully.")
        return redirect("home")

    return render(request, "book.html")

@login_required
def editBooking(request, meetingID):
    meeting = get_object_or_404(Meetings, pk=meetingID)
    return render(request, "editBooking.html", {"meeting":meeting})
