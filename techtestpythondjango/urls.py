from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apihero import viewsets

router = routers.SimpleRouter()
router.register(r"companies", viewsets.CompanyViewSet, basename="Companies")
router.register(r"employees", viewsets.EmployeesViewSet, basename="Employee")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]