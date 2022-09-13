from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_fees  = models.FloatField(default=10000)

