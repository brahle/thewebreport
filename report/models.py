from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Report(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    author = models.ForeignKey(User)
    previous = models.ManyToManyField("self", symmetrical=False, related_name='next', null=True, blank=True)


