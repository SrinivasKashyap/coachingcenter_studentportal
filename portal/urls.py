"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as vs
from teacher import views as vt
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',vs.about,name='about'),
    path('accounts/',vs.accounts,name='accounts'),
    path('', auth_views.LoginView.as_view(template_name='authentication/login.html'), name = 'login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name = 'logout'),
    path('accounts/student/sign_up/',vs.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/teacher/sign_up/',vt.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('student/profile/',vs.StudentDetailView.as_view(), name='student_detail'),
    path('student/courses/',vs.SubjectListView.as_view(), name='student_subjects'),
    path('student/subject/<int:pk>/',vs.StudentSubjectView.as_view(), name='student_subjects_detail'),
    path('student/results/',vs.StudentResultListView.as_view(), name='student_results'),
    path('user/profile/',vt.UpdateProfile, name='update_profile'),
    path('teacher/details/<int:tpk>/',vt.TeacherDetails.as_view(), name='teacher_detail'),
    path('teacher/HomeClass/Results/<int:spk>/<str:cpk>/',vt.HomeClassStudentResult.as_view(), name='class_student_result'),
    path('teacher/HomeClass/StudentList/',vt.HomeClassStudentList.as_view(), name='home_class_students'),
    path('teacher/subject/CourseList/',vt.TeacherCourseList.as_view(), name='teaches_class'),
    path('teacher/subject/results/<int:pk>/',vt.UpdateResults, name='update_result'),
    path('teacher/new_session/',vt.NewSession, name='new_session'),
    path('teacher/HomeClass/',vt.HomeClassCourseList.as_view(), name='home_class_courses'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), name = 'password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name = 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name = 'password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
