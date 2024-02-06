from django.contrib import admin
from django.urls import path
from django.urls import include
# from django.conf.urls import urls
from . import views
from django.urls import re_path
# from ApiApplication import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('expense', views.ExpenseViewSet),
router.register('budget', views.BudgetViewSet)

urlpatterns = [
    path('login', views.login), 
    path('signup', views.signup),
    path('test_token', views.test_token),
    path('',include(router.urls)),
]
