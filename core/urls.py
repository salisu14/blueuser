# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'branch', views.BranchViewSet)
router.register(r'depts', views.DepartmentViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # The API URLs are now determined automatically by the router.
    path('', include(router.urls)),
]