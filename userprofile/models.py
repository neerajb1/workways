from django.db import models
from account.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=120, blank=True)
    empid = models.CharField(max_length=120, blank=True)
    mobile = models.BigIntegerField()
    Salary = models.BigIntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.name
