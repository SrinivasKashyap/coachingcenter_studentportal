from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from django.views.generic import CreateView,View
from django.contrib import messages
from .forms import TeacherSignUpForm,UserUpdateForm,ResultUpdateForm,StudentRollForm,SessionCreate
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.conf import settings
from django.contrib import messages
from student.models import CustomUser,Student,Result,Session
from .models import Teacher,Class,Course,Subject
from django.contrib.auth.decorators import login_required

User=settings.AUTH_USER_MODEL
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'authentication/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request,f'Account created for' + ' ' + username)
        #login(self.request, customUser)
        return redirect('login')

@login_required(login_url='')
def UpdateProfile(request):
    if request.method=="POST":
        form=UserUpdateForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,f'Profile Updated Successfully')
            return redirect('update_profile')
    else:
        form=UserUpdateForm(instance=request.user)
        context={'form':form}
        return render(request, 'teacher/update_profile.html',context)


class HomeClassCourseList(LoginRequiredMixin,View):
    def get(self,request):
        teacher = get_object_or_404(Teacher, user=self.request.user)
        clss=get_object_or_404(Class,teacher=teacher)
        courses=Course.objects.filter(className=clss)
        context={'courses':courses}
        return render(request, 'teacher/home_class_courses.html',context)


class HomeClassStudentResult(LoginRequiredMixin,View):
    def get(self,request,spk=None,cpk=None):                                        #spk=Student pk.    cpk= Course ok
        subject=get_object_or_404(Subject, pk=spk)
        clss=get_object_or_404(Class, name=cpk)
        students=Student.objects.filter(class_studying=clss)
        results=Result.objects.filter(student__in=students, subject=subject).order_by('student__rollno')
        context={'results':results}
        return render(request, 'teacher/students_result.html',context)


class HomeClassStudentList(LoginRequiredMixin,View):
    def get(self,request):
        teacher = get_object_or_404(Teacher, user=self.request.user)
        clss=get_object_or_404(Class,teacher=teacher)
        students=Student.objects.filter(class_studying=clss)
        context={'students':students}
        return render(request, 'teacher/home_class_students.html',context)


class TeacherCourseList(LoginRequiredMixin,View):
    def get(self,request):
        teacher = get_object_or_404(Teacher, user=self.request.user)
        courses=Course.objects.filter(teacher=teacher)
        context={'courses':courses}
        return render(request, 'teacher/course_list.html',context)

class TeacherDetails(LoginRequiredMixin,View):
    def get(self,request, **kwargs):
        context={}                                                     #tpk= teacher pk
        try:
            print('heyybro',kwargs['tpk'])
            teacher=get_object_or_404(Teacher, pk=kwargs['tpk'])
            context['object']=teacher
        except:
            messages.warning(request,f'Teacher does not exist')
        return render(request,'teacher/teacher_detail.html',context)

@login_required(login_url='')
def UpdateResults(request,**kwargs):
    if request.method=="POST":
        flag = request.POST.get('crs_id')
        if flag == None:
            form=StudentRollForm(request.POST)
            course=get_object_or_404(Course, pk=kwargs['pk'])
            if form.is_valid():
                adm=form.cleaned_data.get('rollno')
                try:
                    student=Student.objects.get(rollno=adm,class_studying=course.className)
                    # teacher = get_object_or_404(Teacher, user=self.request.user)
                    r=get_object_or_404(Result, student = student, subject= course.subject)
                    form=ResultUpdateForm(student.pk,course.pk)
                    context={'form': form }
                    # UpdateResults(request,r)
                    return render(request, 'teacher/update_result.html', context)
                except:
                     messages.warning(request,f'Entered RollNo does not exist in your class')
                     form=StudentRollForm()
                     context={'form':form}
                     return render(request, 'teacher/update_result.html',context)

        else:
             print("Updated results received", request.POST)
             rollno=int(request.POST.get('rollno'))
             c=int(request.POST.get('crs_id'))
             course=get_object_or_404(Course, pk=c)
             student=Student.objects.get(rollno= rollno,class_studying=course.className)
             result=Result.objects.get(student = student, subject = course.subject)
             result.rt1_result=float(request.POST.get('rt1_result'))
             result.rt2_result=float(request.POST.get('rt2_result'))
             result.sa1_result=float(request.POST.get('sa1_result'))
             sa2_result=request.POST.get('sa2_result')
             print('waaaaa',sa2_result)

             if sa2_result != "":
                 print('its is  NOT none')
                 result.sa2_result=float(sa2_result)
                 total=(result.rt1_result/2)+(result.rt2_result/2)+result.sa1_result+result.sa2_result
                 result.total=total
                 if total>=90 :
                     grade='A+'
                 elif total>=80 :
                     grade='A'
                 elif total>=70 :
                     grade='B+'
                 elif total>=65 :
                     grade='B'
                 elif total>=60 :
                     grade='C+'
                 elif total>=55:
                     grade='C'
                 elif total>=50:
                     grade='D+'
                 elif total>=40:
                     grade='D'
                 elif total>=30:
                     grade='P'
                 else:
                     grade='F'
                 result.grade=grade

             result.remarks=str(request.POST.get('remarks'))
             result.save()
             messages.success(request,f'Results Updated Successfully')
             form=StudentRollForm()
             context={'form':form}
             return render(request, 'teacher/update_result.html',context)

    else:
        form=StudentRollForm()
        context={'form':form}
        return render(request, 'teacher/update_result.html',context)

@login_required(login_url='')
def NewSession(request):
    if request.method=="POST":
        clss=request.POST['className']
        adm=request.POST['student']
        user =request.user
        student=get_object_or_404(Student, adm_no=adm)
        c=get_object_or_404(Class, name=clss)
        classes=Class.objects.filter(year=c.year)                                 #classes that have the same year eg: 1A,1B..
        try:
            Session.objects.get(className=cl, student=student)
            messages.warning(request,f'Student already exists in the Class')
            teacher=get_object_or_404(Teacher,user=user)
            clss=get_object_or_404(Class,teacher=teacher)
            form=SessionCreate(clss.pk)
            context={'form':form}
            return render(request, 'teacher/new_session.html', context)
        except:
            student.class_studying=c
            student.save()
            Session.objects.create(className=c, student=student)
            messages.success(request,f'Student added to Class')
            teacher=get_object_or_404(Teacher,user=user)
            clss=get_object_or_404(Class,teacher=teacher)
            form=SessionCreate(clss.pk)
            context={'form':form}
            return render(request, 'teacher/new_session.html', context)

    else:
        print('heyy')
        u= request.user
        print('heyy23',u.username)
        teacher=get_object_or_404(Teacher,user=u)
        print('heyy23')
        clss=get_object_or_404(Class,teacher=teacher)
        print('yoyp',clss)
        form=SessionCreate(clss.pk)
        context={'form':form}
        return render(request, 'teacher/new_session.html', context)


# def teachers(request):
#     response = {}
#     response['navbar'] = 'Teachers'
#     if request.method == 'GET':
#         teachers = Teacher.objects.all().order_by('user__first_name')
#
#         response['teachers'] = teachers
#     elif request.method == 'POST':
#         flag = int(request.POST.get('flag1'))
#         if flag == 1:
#             usrname = request.POST['searchUsername']
#             try:
#                 usr = User.objects.get(username=usrname)
#                 teacher = Teacher.objects.get(user=usr)
#             except:
#                 response['error'] = 'No user exist'
#                 return render(request, 'administration/teachers.html',
#                               response)
#
#             # assignment = Assignment.objects. filter(teacher = teacher)
#
#             response['usr'] = usr
#         else:
#
#             # response['assign'] = assignment
#
#             response['register'] = True
#             post_keys = [
#                 'username',
#                 'password1',
#                 'password2',
#                 'last_name',
#                 'first_name',
#                 'age',
#             ]
#             for i in post_keys:
#                 if request.POST[i] == None or request.POST[i] == '':
#                     response['error'] = \
#                         'Could not register try again with correct inputs'
#                     return render(request,
#                                   'administration/teachers.html',
#                                   response)
#             username = request.POST['username'].lower()
#             emailadr = request.POST['email']
#             password = request.POST['password1']
#             password2 = request.POST['password2']
#             first_name = request.POST['first_name']
#             last_name = request.POST['last_name']
#             if password != password2:
#                 response['error'] = "Passwords don\'t match"
#                 return render(request, 'administration/teachers.html',
#                               response)
#             try:
#                 user = \
#                     User.default_manager.get(username_iexact=username.lower())
#                 response['error'] = 'User-Name Already Exists'
#                 return render(request, 'administration/teachers.html',
#                               response)
#             except User.DoesNotExist:
#                 user = User.objects.create_user(username=username,
#                                                 email=emailadr, first_name=first_name,
#                                                 last_name=last_name)
#                 user.set_password(password)
#                 user.save()
#                 profile = Teacher()
#                 profile.user = user
#                 profile.age = int(request.POST['age'])
#                 profile.save()
#                 response['msg'] = 'User created'
#
#         # return redirect('/auth/login')
#
#     return render(request, 'administration/teachers.html', response)
