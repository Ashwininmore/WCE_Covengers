from django.contrib import admin
from .models import UserData

@admin.register(UserData)

class Userdetails(admin.ModelAdmin):
   list_display = ['name','numberPlate','contact','email']