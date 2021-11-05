import django_filters
from apihero.models import Employee

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            'cpf': ['icontains'],
            'name': ['icontains', 'iexact']
        }