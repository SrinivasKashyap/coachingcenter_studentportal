from django.shortcuts import render,get_object_or_404
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView,View,ListView,DetailView,CreateView,UpdateView
from django.contrib import messages
from .forms import StudentSignUpForm
from django.conf import settings
from django.contrib import messages
from .models import Student,Result
from teacher.models import Course,Class,Subject
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

User=settings.AUTH_USER_MODEL
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'authentication/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request,f'Account created for' + ' ' + username)
        return redirect('login')

class SubjectListView(LoginRequiredMixin,View):
    def get(self, request):
        student = get_object_or_404(Student, user=self.request.user)
        clss= get_object_or_404(Class, student=student)
        course=Course.objects.filter(className=clss)
        context = {'courses': course}
        return render(request, 'student/student_subjects.html', context)



# class StudentDetailView(DetailView):
#     model = Student
#     template_name='student/student_detail.html'
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             s=get_object_or_404(Student, user=self.request.user)
#             return s

class StudentDetailView(LoginRequiredMixin,View):
    def get(self, request):
        object = get_object_or_404(Student, user=self.request.user)
        context = {'object': object}
        return render(request, 'student/student_detail.html', context)

class StudentResultListView(LoginRequiredMixin,ListView):
    model = Result
    context_object_name='results'
    template_name='student/student_results.html'
    paginate_by= 5

    # def get_queryset(self,**kwargs):
    #     s=get_object_or_404(Student, adm_no=self.kwargs.get('adm_no'))
    #     return Result.objects.filter(student=s).order_by('subject')
    # model= Result
    # queryset = Result.objects.filter(student.pk=user.student.pk)
    # template_name='student/student_results.html'
    #
    def get_queryset(self):
        if self.request.user.is_authenticated:
            s=get_object_or_404(Student, user=self.request.user)
            return Result.objects.filter(student=s).order_by('subject')
        else:
            return Result.objects.none()

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Result.objects.filter(student=self.request.user.student)
    #     else:
	# 		return Book.objects.none()

class StudentSubjectView(LoginRequiredMixin,View):
    template_name='student/student_subject_detail.html'
    paginate_by= 5

    def get(self,request,**kwargs):
        if self.request.user.is_authenticated:
            s=get_object_or_404(Student, user=self.request.user)
            subject=get_object_or_404(Subject, pk=self.kwargs.get('pk'))
            result= Result.objects.get(student=s,subject=subject )
            context={'result':result}
            return render(request, 'student/student_subject_detail.html', context)
# def register(request):
#     if request.method=="POST":
#         form=StudentSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request,f'Account created for' + ' ' + username)
#             return redirect('student-home')
#     else:
#         form = StudentSignUpForm()
#     return render(request, 'registration/signup_form.html', {'form': form})

def accounts(request):
    return render(request, 'authentication/accounts.html')

def about(request):
    #context = {'posts': Post.objects.all()}
    return render(request, 'student/about.html')
