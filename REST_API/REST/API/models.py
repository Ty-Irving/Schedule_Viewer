from curses.ascii import NUL
from xml.etree.ElementTree import tostring
from django.db import models
from pymysql import NULL


# Create your models here.

# TODO: *** ADD FOREIGN KEYS ***

class DEPARTMENT (models.Model):
    DepartmentNo = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)
    ManagerID = models.ForeignKey('API.MANAGER', on_delete=models.CASCADE)

    class Meta:
        app_label='API'
    
    def __str__(self):
        return self.DepartmentName

class LOGIN (models.Model):
    UserUsername = models.CharField(primary_key=True, max_length=255)
    Password = models.CharField(unique=True, max_length=255)

    class Meta:
        app_label='API'
    
    def __str__(self):
        return self.UserUsername

class USER (models.Model):
    UserId = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=35)
    LName = models.CharField(max_length=35)
    Location = models.CharField(max_length=255)
    DNo = models.ForeignKey(DEPARTMENT, on_delete=models.CASCADE, default=None, null=True, blank=True)
    UserUsername = models.ForeignKey(LOGIN, on_delete=models.CASCADE)

    class Meta:
        app_label='API'

    def __str__(self):
        return self.FName

class MANAGER (models.Model):
    ManagerID = models.ForeignKey(USER, on_delete=models.CASCADE)

    class Meta:
        app_label='API'

    def __str__(self):
        return self.ManagerID.FName

