# from django.test import TestCase
# from django.urls import reverse
# from .models import Employee
# from django_fsm import TransitionNotAllowed

# class EmployeeWorkflowTests(TestCase):

#     def setUp(self):
#         # Create a test employee instance
#         self.employee = Employee.objects.create(
#             name="John Doe",
#             email="john.doe@example.com",
#             performance_review_status="Pending Review"
#         )

#     def test_schedule_review(self):
#         # Test the transition from Pending Review to Review Scheduled
#         url = reverse('schedule_review', args=[self.employee.pk])  # Adjust URL name based on your routing
#         response = self.client.post(url)
        
#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Review Scheduled')
#         self.assertEqual(response.status_code, 200)

#     def test_provide_feedback(self):
#         # Test the transition from Review Scheduled to Feedback Provided
#         self.employee.performance_review_status = 'Review Scheduled'
#         self.employee.save()
        
#         url = reverse('provide_feedback', args=[self.employee.pk])
#         response = self.client.post(url)

#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')
#         self.assertEqual(response.status_code, 200)

#     def test_submit_for_approval(self):
#         # Test the transition from Feedback Provided to Under Approval
#         self.employee.performance_review_status = 'Feedback Provided'
#         self.employee.save()
        
#         url = reverse('submit_for_approval', args=[self.employee.pk])
#         response = self.client.post(url)

#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Under Approval')
#         self.assertEqual(response.status_code, 200)

#     def test_approve_review(self):
#         # Test the transition from Under Approval to Review Approved
#         self.employee.performance_review_status = 'Under Approval'
#         self.employee.save()

#         url = reverse('approve_review', args=[self.employee.pk])
#         response = self.client.post(url)

#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Review Approved')
#         self.assertEqual(response.status_code, 200)

#     def test_reject_review(self):
#         # Test the transition from Under Approval to Review Rejected
#         self.employee.performance_review_status = 'Under Approval'
#         self.employee.save()

#         url = reverse('reject_review', args=[self.employee.pk])
#         response = self.client.post(url)

#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Review Rejected')
#         self.assertEqual(response.status_code, 200)

#     def test_update_feedback(self):
#         # Test the transition from Review Rejected to Feedback Provided
#         self.employee.performance_review_status = 'Review Rejected'
#         self.employee.save()

#         url = reverse('update_feedback', args=[self.employee.pk])
#         response = self.client.post(url)

#         # Assert that the transition is successful
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')
#         self.assertEqual(response.status_code, 200)

#     def test_invalid_transition(self):
#         # Test an invalid transition that shouldn't be allowed
#         self.employee.performance_review_status = 'Feedback Provided'
#         self.employee.save()

#         url = reverse('schedule_review', args=[self.employee.pk])  # Trying to schedule review when already in feedback provided
#         response = self.client.post(url)

#         # Assert that the transition is not allowed
#         self.employee.refresh_from_db()
#         self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')  # Should remain the same
#         self.assertEqual(response.status_code, 400)  # Assuming the server returns 400 on invalid transitions


from django.test import TestCase
from django.urls import reverse
from .models import Employee
from viewflow import exceptions 

class EmployeeWorkflowTests(TestCase):

    def setUp(self):
        # Create a test employee instance
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            performance_review_status="Pending Review"
        )

    def test_schedule_review(self):
        # Test the transition from Pending Review to Review Scheduled
        url = reverse('schedule_review', args=[self.employee.pk])  # Adjust URL name based on your routing
        response = self.client.post(url)
        
        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Review Scheduled')
        self.assertEqual(response.status_code, 200)

    def test_provide_feedback(self):
        # Test the transition from Review Scheduled to Feedback Provided
        self.employee.performance_review_status = 'Review Scheduled'
        self.employee.save()
        
        url = reverse('provide_feedback', args=[self.employee.pk])
        response = self.client.post(url)

        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')
        self.assertEqual(response.status_code, 200)

    def test_submit_for_approval(self):
        # Test the transition from Feedback Provided to Under Approval
        self.employee.performance_review_status = 'Feedback Provided'
        self.employee.save()
        
        url = reverse('submit_for_approval', args=[self.employee.pk])
        response = self.client.post(url)

        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Under Approval')
        self.assertEqual(response.status_code, 200)

    def test_approve_review(self):
        # Test the transition from Under Approval to Review Approved
        self.employee.performance_review_status = 'Under Approval'
        self.employee.save()

        url = reverse('approve_review', args=[self.employee.pk])
        response = self.client.post(url)

        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Review Approved')
        self.assertEqual(response.status_code, 200)

    def test_reject_review(self):
        # Test the transition from Under Approval to Review Rejected
        self.employee.performance_review_status = 'Under Approval'
        self.employee.save()

        url = reverse('reject_review', args=[self.employee.pk])
        response = self.client.post(url)

        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Review Rejected')
        self.assertEqual(response.status_code, 200)

    def test_update_feedback(self):
        # Test the transition from Review Rejected to Feedback Provided
        self.employee.performance_review_status = 'Review Rejected'
        self.employee.save()

        url = reverse('update_feedback', args=[self.employee.pk])
        response = self.client.post(url)

        # Assert that the transition is successful
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')
        self.assertEqual(response.status_code, 200)

    def test_invalid_transition(self):
        # Test an invalid transition that shouldn't be allowed
        self.employee.performance_review_status = 'Feedback Provided'
        self.employee.save()

        url = reverse('schedule_review', args=[self.employee.pk])  # Trying to schedule review when already in feedback provided
        response = self.client.post(url)

        # Assert that the transition is not allowed
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.performance_review_status, 'Feedback Provided')  # Should remain the same
        self.assertEqual(response.status_code, 400)  # Assuming the server returns 400 on invalid transitions

    def test_invalid_transition_with_exception(self):
        # Test invalid transition with Viewflow's FlowException
        self.employee.performance_review_status = 'Feedback Provided'
        self.employee.save()

        try:
            # Try to perform a transition that is not allowed
            url = reverse('schedule_review', args=[self.employee.pk])  # Trying to schedule review when already in feedback provided
            response = self.client.post(url)
            self.fail("Expected FlowException to be raised")  # Fail the test if no exception is raised
        except exceptions.FlowException as e:  # Correctly raise FlowException
            # Assert that FlowException is raised and contains the correct message
            self.assertEqual(str(e), "Transition not allowed")
