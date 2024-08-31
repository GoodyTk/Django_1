from django.db import models 
 
# Create your models here. 
 
class Subject(models.Model): 
    subject = models.CharField(max_length=50) 
 
class Teacher(models.Model): 
    teacher = models.ForeignKey(Subject, on_delete=models.DO_NOTHING) 
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Class(models.Model): 
    name = models.CharField(max_length=50) 
 
class Student(models.Model): 
    student = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    clas = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

class Grade(models.Model):
    grade = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)

    