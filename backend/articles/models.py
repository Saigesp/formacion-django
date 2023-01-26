from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200, default='title')
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now, help_text="fecha de publicación")
    edit_date = models.DateTimeField(default=timezone.now, help_text="fecha de modificación")
    is_draft = models.BooleanField(default=True)
    is_good = models.BooleanField(default=True)

class Comment(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, help_text="fecha de creación")
