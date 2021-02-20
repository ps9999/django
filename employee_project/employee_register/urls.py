from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form, name="employee_insert" ), #localhost:p/employee
    path('<int:id>/', views.employee_form, name="employee_update" ), #localhost:p/employee
    path('list/', views.employee_list, name="employee_list") #localhost:p/employee/list
]