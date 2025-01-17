from django_fsm import transition
from viewflow.views import Flow, Task, Activity, FlowTask, Flow
from viewflow.views import FlowMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review

class ReviewProcess(Flow):
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