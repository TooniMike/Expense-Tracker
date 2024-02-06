from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Expense(models.Model):
    user=models.CharField(max_length=200)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.CharField(max_length=200)
    description=models.TextField(max_length=10000)
    date=models.DateField(auto_now_add=True)

class Budget(models.Model):
    user=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    amount=models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return self.user + '' + self.category