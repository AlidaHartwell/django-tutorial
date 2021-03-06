from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.course_console, name='course_console'),
    path('courses/create', views.course_create, name='course_create'),
    path('courses/<int:course_id>/enroll', views.new_enrollment, name='new_enrollment'),
    path('courses/<int:course_id>/enrollSingle', views.single_enrollment, name='add_single_enrollment'),
    path('courses/<int:course_id>/enrollSingle/submit', views.save_single_enrollment, name='save_single_enrollment'),
    path('courses/<int:course_id>/enroll/status', views.course_enrollment, name='course_enrollment'),
    path('courses/<int:course_id>/assignments', views.assignment_console, name='assignment_console'),
    path('courses/<int:course_id>/assignments/redirect', views.assignment_create, name='assignment_create'),
    path('courses/<int:course_id>/assignments/create', views.assignment_form, name='assignment_form'),
    path('<int:assignment_id>/', views.detail, name='detail'),
    path('student', views.student_intro, name='student_intro'),
    path('student/login', views.student_login, name='student_login'),
    path('student/<int:student_id>/', views.student_console, name='student_console'),
    path('student/<int:student_id>/course/<int:course_id>/assignments', views.student_assignments, name='student_assignments'),
    path('student/<int:student_id>/course/<int:course_id>/assignments/<int:assignment_id>/submissions',
         views.submission_edit,
         name='submission_edit'),
    path('student/<int:student_id>/course/<int:course_id>/assignments/<int:assignment_id>/submissions/<int:submission_id>/save',
         views.submission_file_save,
         name='submission_file_save'),
    path('student/<int:student_id>/course/<int:course_id>/assignments/<int:assignment_id>/submissions/<int:submission_id>/create',
         views.submission_file_create,
         name='submission_file_create'),

]