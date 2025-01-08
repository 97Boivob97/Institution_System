from django.urls import path
from . import views

urlpatterns = [
    
    path('home/',views.home,name="home"),
    path('create_student/',views.create_student,name="create_student"),
    path('create_faculty/',views.create_faculty,name="create_faculty"),
    path('students/',views.student_list,name="student_list"),
    path('faculties/',views.faculty_list,name="faculty_list"),
    path('registration_student/',views.registration_student,name="registration_student"),
    path('login_student/',views.sign_in_student,name="login_student"),
    path('student_home/',views.student_home,name="student_home"),
    path('logout_student/',views.sign_out_student,name="logout_student"),
    path('registration_faculty/',views.registration_faculty,name="registration_faculty"),
    path('login_faculty/',views.sign_in_faculty,name="login_faculty"),
    path('faculty_home/',views.faculty_home,name="faculty_home"),
    path('logout_faculty/',views.sign_out_faculty,name="logout_faculty"),
    path('students/<int:pk>/',views.student_details,name="student_details"),
    path("faculty/<int:pk>/",views.faculty_details,name="faculty_details"),
    path('update_student/<int:pk>/',views.update_student,name="update_student"),
    path("update_faculty/<int:pk>/",views.update_faculty,name="update_faculty"),
    path('delete_student/<int:pk>/',views.delete_student,name="delete_student"),
    path("delete_faculty/<int:pk>/",views.delete_faculty,name="delete_faculty"),
    path('create_course/',views.create_course,name="create_course"),
    path('course_list/',views.course_list,name="course_list"),
    path('create_question/',views.create_question,name="create_question"),
    path('question_list_for_faculty/',views.view_question_list_for_faculty,name="question_list_for_faculty"),
    path('question_list_for_student/',views.view_question_list_for_student,name="question_list_for_student"),
    path('update_question/<int:pk>/',views.update_question,name='update_question'),
    path('attend_exam/',views.attend_exam,name="attend_exam"),
    path('answer_sheet/',views.answer_sheet,name="answer_sheet"),
  

    ]