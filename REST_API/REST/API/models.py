from curses.ascii import NUL
from queue import Empty
from xml.etree.ElementTree import tostring
from django import db
from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint, Q


# Create your models here.

# TODO: *** ADD FOREIGN KEYS ***

class DEPARTMENT (models.Model):
    DepartmentNo = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)
    ManagerID = models.ForeignKey('API.MANAGER', on_delete=models.CASCADE)

    class Meta:
        app_label='API'
    
    def __str__(self):
        return self.DepartmentName + " DepartmentNo: " + str(self.DepartmentNo)

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
        return self.FName + ", UserID: " + str(self.UserId)

class MANAGER (models.Model):
    ManagerID = models.ForeignKey(USER, on_delete=models.CASCADE)
    # Figure out how to make ManagerID a foreign key
    class Meta:
        app_label='API'

    def __str__(self):
        return self.ManagerID.FName + ". ManagerID: " + str(self.ManagerID)

class EMPLOYEE (models.Model):
    EmpID = models.OneToOneField('API.USER', on_delete=models.CASCADE, primary_key=True)
    EmpScheduleID = models.ForeignKey('API.SCHEDULE', on_delete=models.CASCADE)
    Salary = models.FloatField(null=False, default=15.0)

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(Salary__gte=0.0) & Q(Salary__lte=100000000.0), name="my_float_constraint")
        ]

        app_label='API'

    def __str__(self):
        return self.EmpID.FName + ". EmpID: " + str(self.EmpID)

class SCHEDULE (models.Model):
    ScheduleID = models.AutoField(primary_key=True)
    CreatorID = models.ForeignKey('API.MANAGER', on_delete=models.CASCADE)

    class Meta:
        app_label='API'

    def __str__(self):
        return ((self.CreatorID.ManagerID.FName) + " created schedule. ScheduleID: " + str(self.ScheduleID))

class SCHEDULE_SHIFTS (models.Model):
    ScheduleID = models.ForeignKey('API.SCHEDULE', on_delete=models.CASCADE, null=False)
    Date = models.DateField(null=False)
    StartTime = models.TimeField(null=False, default="22:00:00")
    EndTime = models.TimeField(null=False, default="23:00:00")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ScheduleID', 'Date'], name="SchedulePK")
        ]

        app_label='API'

    def __str__(self):
        return "ScheduleID: " + str(self.ScheduleID) + ", Date: " + str(self.Date) + ", StartTime: " + str(self.StartTime)

class REQUEST (models.Model):
    EmpID = models.ForeignKey('API.EMPLOYEE', on_delete=models.CASCADE, null=False)
    Date = models.DateField(null=False)
    Time = models.TimeField(null=False)
    RequestedChange = models.CharField(max_length=255, blank=True, null=True)
    ScheduleID = models.ForeignKey('API.SCHEDULE', on_delete=models.CASCADE, null=False)
    ResolvingMgrID = models.ForeignKey('API.MANAGER', on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['EmpID', 'Date', 'Time'], name="RequestPK")
        ]

        app_label='API'

    def __str__(self):
        return "Emp: " + self.EmpID.EmpID.FName + " " + self.EmpID.EmpID.LName + " Date: " + str(self.Date) + " Time: " + str(self.Time) + ". RequestID: " + str(self.pk)

class TIME_LOG (models.Model):
    EmpID = models.ForeignKey('API.EMPLOYEE', on_delete=models.CASCADE)
    StartTime = models.TimeField(null=False)
    EndTime = models.TimeField(null=False)
    Date = models.DateField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['EmpID', 'StartTime'], name="TimeLogPK")
        ]

        app_label = 'API'
    
    def __str__(self):
        return "Time Log: Employee " + self.EmpID.EmpID.FName + " " + self.EmpID.EmpID.LName + " StartTime: " + str(self.StartTime)

class INVOICE (models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    Amount = models.IntegerField(null=False)
    InvoiceEmpID = models.ForeignKey('API.EMPLOYEE', on_delete=models.CASCADE, null=False)
    InvoiceDate = models.ForeignKey('API.TIME_LOG', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'API'

    def __str__(self):
        return self.InvoiceEmpID.EmpID.FName + " " + self.InvoiceEmpID.EmpID.LName + "'s Invoice on: " + str(self.InvoiceDate.Date)

class PROJECT (models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=255, unique=True, blank=False, null=False)
    ContrllingDepartmentNo = models.ForeignKey('API.DEPARTMENT', on_delete=models.CASCADE, null=False)

    class Meta:
        app_label = 'API'

    def __str__(self):
        return self.ProjectName

class WORKS_ON (models.Model):
    EmpID = models.ForeignKey('API.EMPLOYEE', on_delete=models.CASCADE, null=False)
    ProjectID = models.ForeignKey('API.PROJECT', on_delete=models.CASCADE, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['EmpID', 'ProjectID'], name="WorksOnPK")
        ]

        app_label = 'API'
    
    def __str__(self):
        return self.EmpID.EmpID.FName + " " + self.EmpID.EmpID.LName + " Works On: " +self.ProjectID.ProjectName