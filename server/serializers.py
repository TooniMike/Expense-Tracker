from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Budget
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields = "__all__"
