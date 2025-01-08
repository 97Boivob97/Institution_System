from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=25)
    student_id = models.CharField(max_length=15)
    department = models.TextField(default="")
    gpa = models.DecimalField(max_digits=3,decimal_places=2)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student',null=True,blank=True)

class Faculty(models.Model):
    name = models.CharField(max_length=25)
    designation = models.TextField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty',null=True,blank=True)

class Course(models.Model):
    course_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    instructor = models.CharField(max_length=50)

class Question(models.Model):
    course_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    question = models.TextField(default="")

