from django.db import models

# Create your models here.
class Credentials(models.Model):
    Username = models.CharField(max_length=15)
    Password = models.CharField("password")
    UserID = models.IntegerField("ID", primary_key = True)


class Meetings(models.Model):
    Date = models.DateField("date")
    Time = models.TimeField("time")
    Room = models.IntegerField("room")
    UserID = models.ForeignKey(Credentials, on_delete=models.CASCADE)