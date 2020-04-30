<<<<<<< HEAD
from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,

            'description': self.description,
            'count': self.count,
=======
from django.db import models

class Category(models.Model):
    name =  models.CharField(max_length=200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,

            'description': self.description,
            'count': self.count,
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
        }