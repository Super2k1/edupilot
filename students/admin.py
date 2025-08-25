from django.contrib import admin
from .models import Student,ClassLevel,Enrollment,Attendance

# Register your models here.
admin.site.register(Student)
admin.site.register(ClassLevel)
admin.site.register(Enrollment)
admin.site.register(Attendance)