from django.urls import path, include
from . import views 
from rest_framework import routers
from viewflow.urls import urlpatterns as flow_urlpatterns

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('employee/<int:pk>/schedule-review/', views.schedule_review, name='schedule_review'),
    path('employee/<int:pk>/provide-feedback/', views.provide_feedback, name='provide_feedback'),
    path('employee/<int:pk>/submit-for-approval/', views.submit_for_approval, name='submit_for_approval'),
    path('employee/<int:pk>/approve-review/', views.approve_review, name='approve_review'),
    path('employee/<int:pk>/reject-review/', views.reject_review, name='reject_review'),
    path('employee/<int:pk>/update-feedback/', views.update_feedback, name='update_feedback'),
]


urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<int:company_id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:department_id>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:employee_id>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:review_id>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('employees/<int:employee_id>/review/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:review_id>/schedule/', views.ReviewScheduleView.as_view(), name='review_schedule'),
    path('reviews/<int:review_id>/provide_feedback/', views.ReviewProvideFeedbackView.as_view(), name='review_provide_feedback'),
    path('reviews/<int:review_id>/submit_for_approval/', views.ReviewSubmitForApprovalView.as_view(), name='review_submit_for_approval'),
    path('reviews/<int:review_id>/approve/', views.ReviewApproveView.as_view(), name='review_approve'),
    path('reviews/<int:review_id>/reject/', views.ReviewRejectView.as_view(), name='review_reject'),
    path('reviews/<int:review_id>/update_feedback/', views.ReviewUpdateFeedbackView.as_view(), name='review_update_feedback'),
    path('flow/', include(flow_urlpatterns)),
]