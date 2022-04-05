from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.USER)
admin.site.register(models.LOGIN)
admin.site.register(models.DEPARTMENT)