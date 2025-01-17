from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Review
from django.urls import reverse
from .models import Company, Department, Employee, Project
from .forms import ReviewForm
from viewflow.views import WorkflowViewMixin
from django.contrib.auth.mixins import LoginRequiredMixin


def home_view(request):
    return HttpResponse('Welcome to the Company Management System!')

def schedule_review(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        review_date = request.POST.get('review_date')
        employee.schedule_review(review_date=review_date)
        return redirect('employee_details', employee_id=employee_id)
    context = {'employee': employee}
    return render(request, 'schedule_review.html', context)

def provide_feedback(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        employee.provide_feedback(feedback=feedback)
        return redirect('employee_details', employee_id=employee_id)
    context = {'employee': employee}
    return render(request, 'provide_feedback.html', context)

def submit_for_approval(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.submit_for_approval()
    return redirect('employee_details', employee_id=employee_id)

def approve_review(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.approve_review()
    return redirect('employee_details', employee_id=employee_id)

def reject_review(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.reject_review()
    return redirect('employee_details', employee_id=employee_id)

def update_feedback(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        employee.update_feedback(feedback=feedback)
        return redirect('employee_details', employee_id=employee_id)
    context = {'employee': employee}
    return render(request, 'update_feedback.html', context)

class CompanyListView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/companies.html'

    def get(self, request):
        companies = Company.objects.all()
        context = {'companies': companies}
        return render(request, self.template_name, context)

class CompanyDetailView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/company_details.html'

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        context = {'company': company}
        return render(request, self.template_name, context)

class DepartmentListView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/departments.html'

    def get(self, request):
        departments = Department.objects.all()
        context = {'departments': departments}
        return render(request, self.template_name, context)

class DepartmentDetailView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/department_details.html'

    def get(self, request, department_id):
        department = get_object_or_404(Department, pk=department_id)
        context = {'department': department}
        return render(request, self.template_name, context)

class EmployeeListView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/employees.html'

    def get(self, request):
        employees = Employee.objects.all()
        context = {'employees': employees}
        return render(request, self.template_name, context)

class EmployeeDetailView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/employee_details.html'

    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        context = {'employee': employee}
        return render(request, self.template_name, context)

class ProjectListView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/projects.html'

    def get(self, request):
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, self.template_name, context)

class ProjectDetailView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/project_details.html'

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        context = {'project': project}
        return render(request, self.template_name, context)

class ReviewListView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/reviews.html'

    def get(self, request):
        reviews = Review.objects.all()
        context = {'reviews': reviews}
        return render(request, self.template_name, context)

class ReviewDetailView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/review_details.html'

    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        context = {'review': review}
        return render(request, self.template_name, context)

class ReviewCreateView(LoginRequiredMixin, WorkflowViewMixin):
    template_name = 'myapp/review_form.html'

    def get(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        form = ReviewForm()
        context = {'employee': employee, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, employee_id):
        employee = get_object_or_404(Employee, pk=employee_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.content_object = employee
            review.save()
            return redirect('review_details', review.id)
        context = {'employee': employee, 'form': form}
        return render(request, self.template_name, context)

class ReviewScheduleView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'scheduled'
        review.save()
        return redirect('review_details', review.id)

class ReviewProvideFeedbackView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'feedback_provided'
        review.save()
        return redirect('review_details', review.id)

class ReviewSubmitForApprovalView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'under_approval'
        review.save()
        return redirect('review_details', review.id)

class ReviewApproveView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'approved'
        review.save()
        return redirect('review_details', review.id)

class ReviewRejectView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'rejected'
        review.save()
        return redirect('review_details', review.id)

class ReviewUpdateFeedbackView(LoginRequiredMixin, WorkflowViewMixin):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        review.status = 'feedback_provided'
        review.save()
        return redirect('review_details', review.id)
