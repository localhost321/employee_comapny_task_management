from enum import unique
from django.db import models
from sqlalchemy import null

# Create your models here.

class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)
    company_code=models.IntegerField(unique="True",null="True",blank="True")
    class Meta:
        db_table = "company"

class Employee(models.Model):
    empcode=models.IntegerField(null="True", blank= "True")
    eFname = models.CharField(primary_key='true',max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.CharField(max_length=100)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"
    
class Login(models.Model):
    UserName = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    class Meta:
        db_table = "login"


class Task(models.Model):
    
    taskname = models.CharField(primary_key='true',max_length=50,unique='true',default="")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        db_table = "Task"