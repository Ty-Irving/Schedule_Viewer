from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.USER)
admin.site.register(models.LOGIN)
admin.site.register(models.DEPARTMENT)
admin.site.register(models.MANAGER)
admin.site.register(models.EMPLOYEE)
admin.site.register(models.SCHEDULE)
admin.site.register(models.SCHEDULE_SHIFTS)
admin.site.register(models.REQUEST)
admin.site.register(models.TIME_LOG)
admin.site.register(models.INVOICE)
admin.site.register(models.PROJECT)
admin.site.register(models.WORKS_ON)