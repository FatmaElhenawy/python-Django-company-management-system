from rest_framework import serializers
from .models import Company, Department, Employee, Project

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    assigned_employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'