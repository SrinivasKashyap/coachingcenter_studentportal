from django.db import models
from django.conf import settings
# from student.models import Student
#Create your models here.

class Subject(models.Model):
    name=models.CharField(max_length=20,null=True)
    code=models.CharField(max_length=10,null=True)
    COMPULSORY='C'
    ELECTIVE='E'
    SUBJECT_TYPE_CHOICES=(
    (COMPULSORY,'Compulsory'),
    (ELECTIVE,'Elective')
    )
    subject_type=models.CharField(
    max_length=1,
    choices=SUBJECT_TYPE_CHOICES,
    default=COMPULSORY,
    )

    def __str__(self):
        return self.name + " " + self.code

    class Meta:
        unique_together = ("name", "code")


class Teacher(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,null=False,related_name='teacher',on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, verbose_name='Subjects',null=True,blank=True,default="", on_delete=models.CASCADE)

    def __str__(self):
        if(self.user.first_name):
            return (self.user.first_name + " " + self.user.last_name)
        else:
            return self.user.pk



class Class(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    year=models.PositiveSmallIntegerField()
    teacher=models.OneToOneField(Teacher,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE,default="")
    className=models.ForeignKey(Class, on_delete=models.CASCADE,default="")
    teacher=models.ForeignKey(Teacher,blank=True,null=True,default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.className.name + " " +self.subject.name

    class Meta:
        verbose_name="Course"
        verbose_name_plural="Courses"


# class Notes(model.Model):
#    title=model.CharField(max_length=30,null=False)
#    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
#    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
#    attachment=
