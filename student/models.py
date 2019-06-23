from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from teacher.models import Course,Class,Subject,Teacher
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
# Create your models here.

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(('First name'), max_length=30, blank=False)
    last_name = models.CharField(('Last name'), max_length=30, blank=False)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    class Meta:
        unique_together = ("last_name", "first_name")

class Student(models.Model):
    user=models.OneToOneField(CustomUser, related_name='student',null=False,on_delete=models.CASCADE)
    #first_name=models.CharField(max_length=100,null=True)
    #last_name=models.CharField(max_length=100,null=True)
    adm_no = models.IntegerField(primary_key=True)
    rollno = models.IntegerField(null=False)
    class_studying=models.ForeignKey(Class, verbose_name='Classes',on_delete=models.CASCADE)
    father_name= models.CharField(max_length=100,null=True)
    mother_name= models.CharField(max_length=100,null=True)
    parent_phn= models.CharField(max_length=10,null=False)
    date_join= models.DateField(null=False)
    gender=models.CharField(max_length=10,null=True)
    #subject=models.ManyToManyField(Subject)
    dob = models.DateField(null=False)

    def __str__(self):
        return str(self.rollno) + "-" +self.user.first_name + self.user.last_name

# @receiver(post_save, sender=Student)
# def new_student_result(sender, **kwargs):
#     if kwargs.get('created', False):
# 		# my_group = Group.objects.get(name='Student')
#         student = Student.objects.get(adm_no=kwargs.get('instance').adm_no)
# 		# my_group.user_set.add(student[0].user)
#         courses = Course.objects.filter(className = student.class_studying)
#         studentCreated = student
#         for course in courses:
#             Result.objects.create(student = studentCreated, subject = course.subject)


class Result(models.Model):
    student=models.ForeignKey(Student,null=False,on_delete=models.CASCADE,default="")
    subject=models.ForeignKey(Subject,null=False,on_delete=models.CASCADE,default="")
    #year=models.OneToOneField(Class,null=False,on_delete=models.CASCADE)
    rt1_result=models.FloatField(null=True,default=0.0)
    rt2_result=models.FloatField(null=True,default=0.0)
    sa1_result=models.FloatField(null=True,default=0.0)
    sa2_result=models.FloatField(null=True,default=None)
    total = models.FloatField(null=True,default=None)
    grade = models.CharField(max_length=5,null=True, default="")
    remarks = models.CharField(max_length=100,null=True, default="")


    def __str__(self):
        return self.student.user.username + "-" + self.subject.name

class Session(models.Model):
    className=models.ForeignKey(Class, on_delete=models.CASCADE,default="")
    student=models.ForeignKey(Student, on_delete=models.CASCADE,default="")

    class Meta:
        unique_together = ("className", "student")

@receiver(post_save, sender=Session)
def new_session_result(sender, **kwargs):
    if kwargs.get('created', False):
		# my_group = Group.objects.get(name='Student')
        student = kwargs.get('instance').student
		# my_group.user_set.add(student[0].user)
        courses = Course.objects.filter(className = student.class_studying)
        studentCreated = student
        for course in courses:
            Result.objects.create(student = studentCreated, subject = course.subject)


@receiver(post_save, sender=Student)
def new_student_session_update(sender, **kwargs):
    if kwargs.get('created', False):
		# my_group = Group.objects.get(name='Student')
        student = Student.objects.get(adm_no=kwargs.get('instance').adm_no)
		# my_group.user_set.add(student[0].user)
        studentCreated = student
        Session.objects.create(className = studentCreated.class_studying, student = studentCreated)
