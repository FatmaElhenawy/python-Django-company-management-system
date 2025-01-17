# from django.db import models
# from django_fsm import FSMField, transition
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from viewflow.fsm import FSMField, transition



# class User(AbstractUser):
#     role = models.CharField(max_length=50, choices= [
#         ('Admin', 'Admin'),
#         ('Manager', 'Manager'),
#         ('Employee', 'Employee'),
#     ], default='Employee')

#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         related_name='custom_user_set',  # Add related_name here
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         related_name='custom_user_set',  # Add related_name here
#     )


# class Company(models.Model):
#     company_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.company_name
    
#     @property
#     def departments(self):
#         return self.department_num.count()
    
#     @property
#     def employees(self):
#         return self.employees_num.count()
    
#     @property
#     def projects(self):
#         return self.projects_num.count()
    
# class Department(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     dep_name = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.company.company_name} - {self.dep_name}"
    
#     @property
#     def employees(self):
#         return self.emplyees_num.count()
    
#     @property
#     def projects(self):
#         return self.projects_num.count()
    
# class Employee(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     employee_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     mobile_no = models.CharField(max_length=20)
#     address = models.TextField()
#     designation = models.CharField(max_length=50)
#     hired_on = models.DateField(null=True, blank=True)
#     performance_review_status = FSMField(default='Pending Review')
#     review_date = models.DateField(null=True, blank=True) 
#     feedback = models.TextField(blank=True)  
#     manager_approval = models.BooleanField(default=False) 


#     def __str__(self):
#         return self.employee_name
    
#     @property
#     def days_employed(self):
#         if self.hired_on:
#             from datetime import date
#             today = date.today()
#             return (today - self.hired_on).days
#         return 0
    
#     @transition(field=performance_review_status, source='Pending Review', target='Review Scheduled')
#     def schedule_review(self, review_date):
#         self.review_date = review_date
#         self.save()

#     @transition(field=performance_review_status, source='Review Scheduled', target='Feedback Provided')
#     def provide_feedback(self, feedback):
#         self.feedback = feedback
#         self.save()

#     @transition(field=performance_review_status, source='Feedback Provided', target='Under Approval')
#     def submit_for_approval(self):
#         self.save()

#     @transition(field=performance_review_status, source='Under Approval', target='Review Approved')
#     def approve_review(self):
#         self.manager_approval = True
#         self.save()

#     @transition(field=performance_review_status, source='Under Approval', target='Review Rejected')
#     def reject_review(self):
#         self.save()

#     @transition(field=performance_review_status, source='Review Rejected', target='Feedback Provided')
#     def update_feedback(self):
#         self.save()

# class Project(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     project_name = models.CharField(max_length=100)
#     description = models.TextField
#     start_date = models.DateField()
#     end_date = models.DateField()
#     assigned_employees = models.ManyToManyField(Employee)

#     def __str__(self):
#         return self.project_name

# class Review(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')
    
#     STATUS_CHOICES = (
#         ('pending', 'Pending Review'),
#         ('scheduled', 'Review Scheduled'),
#         ('feedback_provided', 'Feedback Provided'),
#         ('under_approval', 'Under Approval'),
#         ('approved', 'Review Approved'),
#         ('rejected', 'Review Rejected'),
#     )
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     feedback = models.TextField(blank=True)
#     review_date = models.DateField(null=True, blank=True)
    
#     def __str__(self):
#         return f"Review for {self.content_object}"

# class ReviewFlow(Flow):
#     process_class = 'myapp.flow.ReviewProcess'

#     start = Task(
#         'Start',
#         activity=Activity(
#             'Start',
#             transition('schedule_review'),
#         ),
#     )

#     schedule_review = Task(
#         'Schedule Review',
#         activity=Activity(
#             'Schedule Review',
#             transition('provide_feedback'),
#         ),
#     )

#     provide_feedback = Task(
#         'Provide Feedback',
#         activity=Activity(
#             'Provide Feedback',
#             transition('submit_for_approval'),
#         ),
#     )

#     submit_for_approval = Task(
#         'Submit for Approval',
#         activity=Activity(
#             'Submit for Approval',
#             transition('approve'),
#             transition('reject'),
#         ),
#     )

#     approve = Task(
#         'Approve',
#         activity=Activity(
#             'Approve',
#             transition('finish'),
#         ),
#     )

#     reject = Task(
#         'Reject',
#         activity=Activity(
#             'Reject',
#             transition('update_feedback'),
#         ),
#     )

#     update_feedback = Task(
#         'Update Feedback',
#         activity=Activity(
#             'Update Feedback',
#             transition('submit_for_approval'),
#         ),
#     )

#     finish = Task(
#         'Finish',
#         activity=Activity(
#             'Finish',
#         ),
#     )

#     review = FlowTask(
#         'Review',
#         review.status,
#         transition('schedule_review'),
#         transition('provide_feedback'),
#         transition('submit_for_approval'),
#         transition('approve'),
#         transition('reject'),
#         transition('update_feedback'),
#         transition('finish'),
#     )

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django_fsm import FSMField, transition
from viewflow.views import Flow, Task, Activity, FlowTask

class Company(models.Model):
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.employee_name

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.project_name

class Review(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    STATUS_CHOICES = (
        ('pending', 'Pending Review'),
        ('scheduled', 'Review Scheduled'),
        ('feedback_provided', 'Feedback Provided'),
        ('under_approval', 'Under Approval'),
        ('approved', 'Review Approved'),
        ('rejected', 'Review Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    feedback = models.TextField(blank=True)
    review_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Review for {self.content_object}"

class CustomUser(AbstractUser):
    # Add any additional fields you need for your user model
    pass

class ReviewFlow(Flow):
    process_class = 'myapp.flow.ReviewProcess'

    start = Task(
        'Start',
        activity=Activity(
            'Start',
            transition('schedule_review'),
        ),
    )

    schedule_review = Task(
        'Schedule Review',
        activity=Activity(
            'Schedule Review',
            transition('provide_feedback'),
        ),
    )

    provide_feedback = Task(
        'Provide Feedback',
        activity=Activity(
            'Provide Feedback',
            transition('submit_for_approval'),
        ),
    )

    submit_for_approval = Task(
        'Submit for Approval',
        activity=Activity(
            'Submit for Approval',
            transition('approve'),
            transition('reject'),
        ),
    )

    approve = Task(
        'Approve',
        activity=Activity(
            'Approve',
            transition('finish'),
        ),
    )

    reject = Task(
        'Reject',
        activity=Activity(
            'Reject',
            transition('update_feedback'),
        ),
    )

    update_feedback = Task(
        'Update Feedback',
        activity=Activity(
            'Update Feedback',
            transition('submit_for_approval'),
        ),
    )

    finish = Task(
        'Finish',
        activity=Activity(
            'Finish',
        ),
    )

    review = FlowTask(
        'Review',
        Review.status,
        transition('schedule_review'),
        transition('provide_feedback'),
        transition('submit_for_approval'),
        transition('approve'),
        transition('reject'),
        transition('update_feedback'),
        transition('finish'),
    )