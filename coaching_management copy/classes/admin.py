# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CustomUser, Course, Registration

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Registration)
