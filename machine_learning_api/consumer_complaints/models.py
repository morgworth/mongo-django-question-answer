from django.db import models


class Complaint(models.Model):
    text = models.TextField()
    type = models.CharField(max_length=100, blank=True, default='')
