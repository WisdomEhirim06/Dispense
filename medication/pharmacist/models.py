from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Drug(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    composition = models.TextField
    indications = models.TextField
    interactions = models.TextField
    dosage = models.TextField
    side_effects = models.TextField

    def __str__(self):
        return self.name

class DrugHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.search_query}"