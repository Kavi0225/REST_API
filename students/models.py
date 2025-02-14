from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=50)
    emp_branch = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name
    