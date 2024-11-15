from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Admin,User



admin.site.register(Admin)
admin.site.register(User)