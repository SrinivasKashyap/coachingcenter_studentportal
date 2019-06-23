from django.contrib import admin
from .models import Student,Result,CustomUser
# Register your models here.
admin.site.register(Student)
admin.site.register(Result)
admin.site.register(CustomUser)
