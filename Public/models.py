from django.db import models

# Create your models here.
class Meetings(models.Model):
    date = models.DateTimeField("Date and Time")
    room = models.IntegerField("room")
    def __str__(self):
        return str(self.date)