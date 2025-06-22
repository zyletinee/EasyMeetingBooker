from django.db import models

# Create your models here.
class Credentials(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField("password")
    userID = models.IntegerField("ID", primary_key = True)
    def __str__(self):
        return self.username


class Meetings(models.Model):
    date = models.DateTimeField("Date and Time")
    room = models.IntegerField("room")
    userID = models.ForeignKey(Credentials, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date)