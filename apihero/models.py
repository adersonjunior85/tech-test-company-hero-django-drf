from django.db import models

class Company(models.Model):
    cnpj = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.cnpj

class Employee(models.Model):
    name = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    companies = models.ManyToManyField(Company, related_name='employees')

    def __str__(self):
        return self.name