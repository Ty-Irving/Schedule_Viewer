from django.db import models

# Create your models here.

class User (models.Model):
    UserId = models.AutoField(primary_key=True)
    FName = models.CharField(max_length=35)
    LName = models.CharField(max_length=35)
    Location = models.CharField(max_length=255)
    DNo = models.IntegerField(null=True)
    UserUsername = models.CharField(max_length=255)

    class Meta:
        app_label='API'

    def __str__(self):
        return self.UserUsername