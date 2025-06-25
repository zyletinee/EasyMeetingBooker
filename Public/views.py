# Create your views here.

from .models import Meetings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware
from datetime import timedelta
from django.utils import timezone

def index(request):
    return render(request, "index.html")

@login_required
def home(request):
    upcomingMeetings = Meetings.objects.order_by("date")[:3]
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
    bookings = Meetings.objects.filter(userID=request.user).order_by('date')
    return render(request, 'viewBooking.html', {'bookings': bookings})

@login_required
def book(request):
    if request.method == 'POST':
        date_str = request.POST.get('bookingDate')
        room = request.POST.get('roomSelection')
        # Checking all fields filled
        if not date_str or not room:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'book.html')
        
        # Checking if date information is correct
        try:
            bookingDate = timezone.datetime.fromisoformat(date_str)
            bookingDate = timezone.make_aware(bookingDate)
        except ValueError:
            messages.error(request, "Invalid date format.")
            return render(request, 'book.html')

        room = int(room)

        # Check for meetings before or after inputted time
        beforeMeeting = bookingDate - timedelta(hours=1)
        afterMeeting = bookingDate + timedelta(hours=1)

        overlap = Meetings.objects.filter(
            room=room,
            date__range=(beforeMeeting, afterMeeting)
        ).exists()

        if overlap:
            messages.error(request, "This room is already booked within an hour of your selected time.")
            return render(request, 'book.html')

        # Save the meeting
        Meetings.objects.create(userID=request.user, date=bookingDate, room=room)
        messages.success(request, "Booking successful!")
        return redirect('viewBooking')
    return render(request, 'book.html')

@login_required
def editBooking(request, meetingID):
 # Get the meeting and ensure it belongs to the logged-in user
    meeting = get_object_or_404(Meetings, id=meetingID, userID=request.user)

    if request.method == 'POST':
        date_str = request.POST.get('bookingDate')
        room = request.POST.get('roomSelection')

        # Check all fields are filled
        if not date_str or not room:
            messages.error(request, "Please fill in all fields.")
            return render(request, 'editBooking.html', {'meeting': meeting})

        try:
            bookingDate = timezone.datetime.fromisoformat(date_str)
            bookingDate = timezone.make_aware(bookingDate)
        except ValueError:
            messages.error(request, "Invalid date format.")
            return render(request, 'editBooking.html', {'meeting': meeting})

        room = int(room)

        # Check for meetings before or after inputted time
        beforeMeeting = bookingDate - timedelta(hours=1)
        afterMeeting = bookingDate + timedelta(hours=1)

        overlap = Meetings.objects.filter(
            room=room,
            date__range=(beforeMeeting, afterMeeting)
        ).exists()

        if overlap:
            messages.error(request, "This room is already booked within an hour of your new time.")
            return render(request, 'editBooking.html', {'meeting': meeting})

        # Update the meeting
        meeting.date = bookingDate
        meeting.room = room
        meeting.save()

        messages.success(request, "Booking updated successfully!")
        return redirect('viewBooking')
    return render(request, 'editBooking.html', {'meeting': meeting})
