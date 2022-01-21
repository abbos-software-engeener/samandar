from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    birthdays = models.DateField()
    skill = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)