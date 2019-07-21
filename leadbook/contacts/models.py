from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=2000)
    country=models.CharField(max_length=2000)
    revenue=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.name