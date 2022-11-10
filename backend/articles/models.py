from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, default='title')
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, help_text="fecha de publicación")
    is_draft = models.BooleanField(default=True)
