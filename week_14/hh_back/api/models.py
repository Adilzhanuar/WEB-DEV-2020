from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=200)
    address = models.TextField(default='')


    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city
        }
    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="")
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary:': self.salary
        }
    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }



