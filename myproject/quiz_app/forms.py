from django import forms
from . models import Student,Faculty,Course,Question

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"