from django.contrib import admin
from .models import Teacher,Subject,Class,Course
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Course)
