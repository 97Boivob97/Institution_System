from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Student,Faculty,Course,Question
from .forms import StudentForm,FacultyForm,CourseForm,QuestionForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib import messages
from django.http import HttpResponse

class RegisterStudent(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class RegisterFaculty(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

@login_required
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = StudentForm()
    context = {
        "form":form,
    }
    return render(request,'student.html',context)

@login_required
def create_faculty(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = FacultyForm()
    context = {
        "form":form,
    }
    return render(request,'faculty.html',context)

@login_required
def student_list(request):
    students = Student.objects.all()
    context = {
        "students":students
    }
    return render(request,'student_list.html',context)

@login_required
def faculty_list(request):
    faculties = Faculty.objects.all()
    context = {
        "faculties":faculties
    }
    return render(request,'faculty_list.html',context)

@login_required
def student_details(request,pk):
    try:
        student = Student.objects.get(pk=pk)
        context={
            "student":student,
        }
        return render(request,'student_details.html',context)
    except Student.DoesNotExist:
        return HttpResponse(f"Student {pk} does not exists!")
    
@login_required   
def faculty_details(request,pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
        context={
            "faculty":faculty,
        }
        return render(request,'faculty_details.html',context)
    except Faculty.DoesNotExist:
        return HttpResponse(f"Faculty {pk} does not exists!")
    
@login_required   
def update_student(request,pk):
    try:
        student = Student.objects.get(pk=pk)
        if request.method == "POST":
         form = StudentForm(request.POST,instance=student)
         if form.is_valid():
             form.save()
             return redirect('student_list')
        form = StudentForm(instance=student)
        context = {"form":form}
        return render(request,'update_student.html',context)
    except Student.DoesNotExist:
        return HttpResponse(f"Student {pk} does not exists!")
    
@login_required    
def update_faculty(request,pk):
    try:
        student = Faculty.objects.get(pk=pk)
        if request.method == "POST":
         form = FacultyForm(request.POST,instance=student)
         if form.is_valid():
             form.save()
             return redirect('faculty_list')
        form = FacultyForm(instance=student)
        context = {"form":form}
        return render(request,'update_faculty.html',context)
    except Faculty.DoesNotExist:
        return HttpResponse(f"Faculty {pk} does not exists!")
    
@login_required   
def delete_student(request,pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('student_list')
    except Student.DoesNotExist:
        return HttpResponse(f"Student {pk} does not exists!!")
@login_required   
def delete_faculty(request,pk):
    try:
        faculty = Faculty.objects.get(pk=pk)
        faculty.delete()
        return redirect('faculty_list')
    except Faculty.DoesNotExist:
        return HttpResponse(f"faculty {pk} does not exists!!")


@login_required
def student_home(request):
    return render(request,'student_home.html')

def registration_student(request):
    if request.method == "POST":
        form = RegisterStudent(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login_student')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterStudent()

    return render(request, 'registration_student.html', {'form': form})
    
def sign_in_student(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_home')
        else:
            return render(request, 'login_student.html', {"form": form})
    else:
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, 'login_student.html', context)
    
@login_required   
def sign_out_student(request):
    logout(request) 
    return redirect('login_student')

@login_required
def faculty_home(request):
    return render(request,'faculty_home.html')


def registration_faculty(request):
    if request.method == "POST":
        form = RegisterFaculty(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login_faculty')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterFaculty()

    return render(request, 'registration_faculty.html', {'form': form})


def sign_in_faculty(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('faculty_home')
    else:
        form = AuthenticationForm()
        context = {"form":form}
        return render(request,'login_faculty.html',context)
    

@login_required   
def sign_out_faculty(request):
    logout(request) 
    return redirect('login_faculty')

@login_required 
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_home')
    form = CourseForm()
    context = {
        "form":form,
    }
    return render(request,'create_course.html',context)

@login_required 
def course_list(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    return render(request,'course_list.html',context)

@login_required
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_home')
    form = QuestionForm()
    context = {"form":form,}
    return render(request,'create_question.html',context)
    
@login_required   
def view_question_list_for_faculty(request):
    questions = Question.objects.all()
    context={"questions":questions,}
    return render(request,'question_list_for_faculty.html',context)

@login_required   
def view_question_list_for_student(request):
    questions = Question.objects.all()
    context={"questions":questions,}
    return render(request,'question_list_for_student.html',context)

@login_required 
def update_question(request,pk):
    question = Question.objects.get(pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST,instance=question)
        if form.is_valid():
            form.save()
            return redirect('question_list_for_faculty')
    form = QuestionForm(instance=question)
    context = {"form":form,}
    return render(request,'update_question.html',context)



@login_required
def attend_exam(request):
    return render(request,'attend_exam.html')

@login_required
def answer_sheet(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        student_id = request.GET.get('student_id', '')
        course_title = request.GET.get('course_title', '')
        course_code = request.GET.get('course_code', '')
        section = request.GET.get('section', '')
        instructor = request.GET.get('instructor', '')
        answer = request.GET.get('answer', '')

        return render(request, 'answer_sheet.html', {
            'name': name,
            'student_id': student_id,
            'course_title': course_title,
            'course_code': course_code,
            'section': section,
            'instructor': instructor,
            'answer': answer,
        })
    return render(request, 'attend_exam.html')

       



