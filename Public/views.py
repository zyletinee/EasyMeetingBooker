# Create your views here.

from django.http import HttpResponse
from .models import Meetings
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request, "index.html")

def home(request):
    upcomingMeetings = Meetings.objects.order_by("-Date")[:3]
    context = {"upcomingMeetings":upcomingMeetings}
    return render(request, "home.html", context)

def signUp(request):
    return render(request, "signUp.html")

def login(request):
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
