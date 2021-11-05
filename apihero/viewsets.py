from django.db import models
from rest_framework import viewsets
from apihero import serializers
from apihero.models import Company, Employee
from rest_framework.response import Response
from django_filters import rest_framework as filters
from apihero.filters import EmployeeFilter
from rest_framework.decorators import action

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = Company.objects.all()

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeerSerializer
    queryset = Employee.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter
    lookup_field = 'cpf'

    @action(methods=['get','post'], detail=True)
    def companies(self, request , cpf=None, **kwargs):
        employee: Employee = Employee.objects.get(cpf=cpf) 
        if (request.method == 'GET'):
            return Response(serializers.CompanySerializer(Company.objects.filter(employees=employee), many=True).data)
        if (request.method == 'POST'):
            company = Company.objects.filter(id=request.data.get('company')).first()
            if not company:
                company = Company(request.data)
                company.save()
            employee.companies.add(company)
            return Response(serializers.CompanySerializer(company).data)