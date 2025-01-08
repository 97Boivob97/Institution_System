# Generated by Django 5.1.4 on 2025-01-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_faculty_user_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('instructor', models.CharField(max_length=50)),
            ],
        ),
    ]
