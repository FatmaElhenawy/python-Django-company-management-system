from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Company, Department, Employee, Project
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, ProjectSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def schedule_review(self, request, pk=None):
        employee = self.get_object()
        review_date = request.data.get('review_date')
        employee.schedule_review(review_date=review_date)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def provide_feedback(self, request, pk=None):
        employee = self.get_object()
        feedback = request.data.get('feedback')
        employee.provide_feedback(feedback = feedback)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def submit_for_approval(self, request, pk=None):
        employee = self.get_object()
        employee.submit_for_approval()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def approve_review(self, request, pk=None):
        employee = self.get_object()
        employee.approve_review()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reject_review(self, request, pk=None):
        employee = self.get_object()
        employee.reject_review()
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def update_feedback(self, request, pk=None):
        employee = self.get_object()
        feedback = request.data.get('feedback')
        employee.update_feedback(feedback=feedback)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]