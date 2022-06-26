from django.db import models


# Create your models here.

class UserData(models.Model):
    name=models.CharField(max_length=30)
    numberPlate = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    file = models.FileField(upload_to='media', null=True)
    title = models.CharField(max_length=50, null=True)

    def _str_(self):
        return self.title