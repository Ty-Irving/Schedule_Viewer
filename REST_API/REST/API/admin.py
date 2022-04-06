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