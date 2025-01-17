from django.db import models
from django_fsm import FSMField, transition

class Company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
    
    @property
    def departments(self):
        return self.department_num.count()
    
    @property
    def employees(self):
        return self.employees_num.count()
    
    @property
    def projects(self):
        return self.projects_num.count()
    
class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company.company_name} - {self.dep_name}"
    
    @property
    def employees(self):
        return self.emplyees_num.count()
    
    @property
    def projects(self):
        return self.projects_num.count()
    
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    designation = models.CharField(max_length=50)
    hired_on = models.DateField(null=True, blank=True)
    performance_review_status = FSMField(default='Pending Review')
    review_date = models.DateField(null=True, blank=True) 
    feedback = models.TextField(blank=True)  
    manager_approval = models.BooleanField(default=False) 


    def __str__(self):
        return self.employee_name
    
    @property
    def days_employed(self):
        if self.hired_on:
            from datetime import date
            today = date.today()
            return (today - self.hired_on).days
        return 0
    
    @transition(field=performance_review_status, source='Pending Review', target='Review Scheduled')
    def schedule_review(self, review_date):
        self.review_date = review_date
        self.save()

    @transition(field=performance_review_status, source='Review Scheduled', target='Feedback Provided')
    def provide_feedback(self, feedback):
        self.feedback = feedback
        self.save()

    @transition(field=performance_review_status, source='Feedback Provided', target='Under Approval')
    def submit_for_approval(self):
        self.save()

    @transition(field=performance_review_status, source='Under Approval', target='Review Approved')
    def approve_review(self):
        self.manager_approval = True
        self.save()

    @transition(field=performance_review_status, source='Under Approval', target='Review Rejected')
    def reject_review(self):
        self.save()

    @transition(field=performance_review_status, source='Review Rejected', target='Feedback Provided')
    def update_feedback(self):
        self.save()

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.project_name