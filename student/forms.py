from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.conf import settings
from .models import Student,CustomUser
from teacher.models import Class

#User=settings.AUTH_USER_MODEL

class StudentSignUpForm(UserCreationForm):
#starts here
    adm_no = forms.IntegerField(required=True)
    rollno = forms.IntegerField(required=True)
    class_studying=forms.ModelChoiceField(queryset=Class.objects.all(),
                                            label=('Classes'))
    father_name= forms.CharField(max_length=100,required=True, label=('Father Name'))
    mother_name= forms.CharField(max_length=100,required=True, label=('Mother Name'))
    parent_phn= forms.CharField(max_length=10,required=True, label=('Parent Phonenumber'))
    date_join= forms.DateField(required=True,label=('Date of Joining'))
    gender=forms.CharField(max_length=10,required=False,label=('Gender'))
    dob = forms.DateField(required=True,label=('Date of Birth'))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields=['username','first_name','last_name','email','password1','password2','adm_no','rollno','class_studying','father_name','mother_name','parent_phn','date_join','gender','dob',]

    @transaction.atomic
    def save(self):
       user = super(StudentSignUpForm, self).save(commit=False)
       user.is_student = True
       user.save()
       student = Student.objects.create(user=user,adm_no=self.cleaned_data.get('adm_no'),
                                       rollno=self.cleaned_data.get('rollno'),
                                       class_studying=self.cleaned_data.get('class_studying'),
                                       father_name=self.cleaned_data.get('father_name'),
                                       mother_name=self.cleaned_data.get('mother_name'),
                                       parent_phn=self.cleaned_data.get('parent_phn'),
                                       date_join=self.cleaned_data.get('date_join'),
                                       gender=self.cleaned_data.get('date_join'),
                                       dob=self.cleaned_data.get('dob')
       )

       return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username','email']
