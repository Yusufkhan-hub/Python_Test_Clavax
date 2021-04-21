from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Student(models.Model):
    
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pin = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    email=models.EmailField( max_length=54)
    class_opted = models.IntegerField()
    marks = models.IntegerField()
    date_enrolled = models.DateField(auto_now_add=True)
