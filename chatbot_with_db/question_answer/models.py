from django.db import models

# Create your models here.

class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    keywords = models.TextField(default='')
    category = models.CharField(max_length=100, default='uncategorized')
