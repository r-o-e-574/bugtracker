from django.contrib import admin
from bugtracker.models import MyUser, Ticket
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(MyUser, UserAdmin)
admin.site.register(Ticket)