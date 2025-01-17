from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'companies', views.CompanyViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'projects', views.ProjectViewSet)


urlpatterns = [
    path('', include(router.urls)),  
]