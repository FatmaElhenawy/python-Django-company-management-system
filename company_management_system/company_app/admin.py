from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'performance_review_status']
    
admin.site.register(Employee, EmployeeAdmin)
