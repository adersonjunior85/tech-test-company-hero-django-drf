from rest_framework import serializers
from apihero.models import Company,Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Company
        fields=["id","nome","cnpj","site","email","endereco","telefone","employees"]
        depth = 1 
    
class EmployeerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields='__all__'
        depth = 2 