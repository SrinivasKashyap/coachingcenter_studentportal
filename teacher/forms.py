from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.conf import settings
from student.models import *
from teacher.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

User=settings.AUTH_USER_MODEL

class TeacherSignUpForm(UserCreationForm):
    subject=forms.ModelChoiceField(queryset=Subject.objects.all().order_by('name'),
                                            label=('Subjects'))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields=['username','first_name','last_name','email','password1','password2','subject',]

    @transaction.atomic
    def save(self,*args,**kwargs):
       user = super(TeacherSignUpForm, self).save(commit=False)
       user.is_teacher = True
       user.save()
       teacher = Teacher.objects.create(user=user,subject=self.cleaned_data.get('subject'),
       )

       return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username','email','image']

class ResultUpdateForm(forms.Form):
    flag1=0
    rollno=forms.IntegerField()
    crs_id=forms.IntegerField()
    rt1_result=forms.FloatField(label='Rt1 Results')
    rt2_result=forms.FloatField(label='Rt2 Results',min_value=0,max_value=20)
    sa1_result=forms.FloatField(label='Sa1 Results',min_value=0,max_value=30)
    sa2_result=forms.FloatField(label='Sa2 Results',min_value=0,max_value=50,required=False)
    total=forms.FloatField(label='Total')
    grade=forms.CharField(max_length=5,label='Grade')
    remarks=forms.CharField(label='Remarks')
    def __init__(self,*args,**kwargs):
        course=Course.objects.get(pk=args[1])
        student=Student.objects.get(adm_no=args[0],class_studying=course.className)
        result=Result.objects.get(student= student, subject=course.subject)
        super(ResultUpdateForm,self).__init__()
        self.fields['rollno'].widget = forms.HiddenInput(attrs = {'value': student.rollno})
        self.fields['crs_id'].widget = forms.HiddenInput(attrs = {'value': course.pk})
        self.fields['rt1_result'].widget = forms.NumberInput(attrs = {'value': result.rt1_result , 'step':"0.01"})
        self.fields['rt2_result'].widget = forms.NumberInput(attrs = {'value': result.rt2_result, 'step': "0.01"})
        self.fields['sa1_result'].widget = forms.NumberInput(attrs = {'value': result.sa1_result, 'step': "0.01"})
        self.fields['sa2_result'].widget = forms.NumberInput(attrs = {'value': result.sa2_result, 'step': "0.01"})
        self.fields['total'].widget = forms.NumberInput(attrs = {'value': result.total})
        self.fields['total'].widget.attrs['readonly']=True
        self.fields['grade'].widget = forms.TextInput(attrs = {'value': result.grade})
        self.fields['grade'].widget.attrs['readonly']=True
        self.fields['remarks'].widget = forms.TextInput(attrs = {'value': result.remarks})
    # def save(self):
    #     pass:

    # class Meta:
    #     model = Result
    #     fields = ['rollno','rt1_result']#,'rt2_result','sa1_result','sa2_result','total','grade','remarks',]

class StudentRollForm(forms.Form):
    rollno=forms.IntegerField(label='Roll Number')
    flag1=1

# class SessionCreate(forms.Form):
#     className=forms.CharField()
#     student_adm=forms.IntegerField()
#     def __init__(self,*args,**kwargs):
#         super(SessionCreate,self).__init__()
#         self.fields['className'].widget = forms.TextInput(attrs = {'value': args[0]})
#         self.fields['className'].widget.attrs['readonly']=True

class SessionCreate(forms.ModelForm):

    class Meta:
        model = Session
        fields=['className','student']

    def __init__(self,*args,**kwargs):
        super(SessionCreate,self).__init__()
        self.fields['className'].widget = forms.TextInput(attrs = {'value': args[0]})
        self.fields['className'].widget.attrs['readonly']=True
