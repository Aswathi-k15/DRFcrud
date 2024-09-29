from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('employees', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),

]