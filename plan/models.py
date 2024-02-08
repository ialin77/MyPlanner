from django.db import models
from django.contrib.auth.models import User



class Plan(models.Model):

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    date = models.CharField(max_length=10, null=True, blank=True)
    time = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title