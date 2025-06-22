from django.contrib import admin

# Register your models here.

from .models import Meetings, Credentials

admin.site.register(Meetings)
admin.site.register(Credentials)