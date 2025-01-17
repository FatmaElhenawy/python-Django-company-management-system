from django.test import TestCase
from rest_framework.test import APIClient
from .models import Company, Department, Employee, Project
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, ProjectSerializer
from django.contrib.auth.models import User

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test data
        self.company = Company.objects.create(company_name='Test Company')
        self.department = Department.objects.create(company=self.company, department_name='Test Department')
        self.employee = Employee.objects.create(company=self.company, department=self.department, employee_name='Test Employee', email_address='test@example.com')
        self.project = Project.objects.create(company=self.company, department=self.department, project_name='Test Project')
        self.project.assigned_employees.add(self.employee)

    def test_company_list(self):
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_company_create(self):
        data = {'company_name': 'New Test Company'}
        response = self.client.post('/api/companies/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['company_name'], 'New Test Company')

    def test_department_list(self):
        response = self.client.get('/api/departments/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_department_create(self):
        data = {'company': self.company.id, 'department_name': 'New Test Department'}
        response = self.client.post('/api/departments/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['department_name'], 'New Test Department')

    def test_employee_list(self):
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_employee_create(self):
        data = {'company': self.company.id, 'department': self.department.id, 'employee_name': 'New Test Employee', 'email_address': 'newtest@example.com'}
        response = self.client.post('/api/employees/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['employee_name'], 'New Test Employee')

    def test_employee_schedule_review(self):
        data = {'review_date': '2024-03-15'}
        response = self.client.post(f'/api/employees/{self.employee.id}/schedule_review/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Review Scheduled')
        self.assertEqual(response.data['review_date'], '2024-03-15')

    def test_employee_provide_feedback(self):
        data = {'feedback': 'Great work!'}
        response = self.client.post(f'/api/employees/{self.employee.id}/provide_feedback/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Feedback Provided')
        self.assertEqual(response.data['feedback'], 'Great work!')

    def test_employee_submit_for_approval(self):
        self.employee.provide_feedback(feedback='Great work!')
        self.employee.save()
        response = self.client.post(f'/api/employees/{self.employee.id}/submit_for_approval/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Under Approval')

    def test_employee_approve_review(self):
        self.employee.provide_feedback(feedback='Great work!')
        self.employee.submit_for_approval()
        self.employee.save()
        response = self.client.post(f'/api/employees/{self.employee.id}/approve_review/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Review Approved')
        self.assertEqual(response.data['manager_approval'], True)

    def test_employee_reject_review(self):
        self.employee.provide_feedback(feedback='Great work!')
        self.employee.submit_for_approval()
        self.employee.save()
        response = self.client.post(f'/api/employees/{self.employee.id}/reject_review/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Review Rejected')

    def test_employee_update_feedback(self):
        self.employee.provide_feedback(feedback='Great work!')
        self.employee.submit_for_approval()
        self.employee.reject_review()
        self.employee.save()
        data = {'feedback': 'Updated feedback'}
        response = self.client.post(f'/api/employees/{self.employee.id}/update_feedback/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['performance_review_status'], 'Feedback Provided')
        self.assertEqual(response.data['feedback'], 'Updated feedback')

    def test_project_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_project_create(self):
        data = {'company': self.company.id, 'department': self.department.id, 'project_name': 'New Test Project'}
        response = self.client.post('/api/projects/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['project_name'], 'New Test Project')