from django.contrib import admin
from accounts.models import SchoolManagement
from .models import StudentRegisteration

admin.site.register(SchoolManagement)
admin.site.register(StudentRegisteration)