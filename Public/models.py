from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meetings(models.Model):
    date = models.DateTimeField("Date and Time")
    room = models.IntegerField("room")
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.date)