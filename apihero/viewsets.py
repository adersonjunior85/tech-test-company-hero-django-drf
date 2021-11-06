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
    lookup_field = 'id'

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeerSerializer
    queryset = Employee.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EmployeeFilter    
    lookup_field = 'name'   
    @action(methods=['get','post'], detail=True)
    def companies(self, request , name=None, **kwargs):
        employee: Employee = Employee.objects.get(name=name) 
        if (request.method == 'GET'):
            return Response(serializers.CompanySerializer(Company.objects.filter(employees=employee), many=True).data)
        if (request.method == 'POST'):
            company = Company.objects.filter(cnpj=request.data.get('cnpj')).first()
            if not company:
                company = Company(request.data)
                company.save()
            employee.companies.add(company)
            return Response(serializers.CompanySerializer(company).data)