from django.db import models
from datetime import datetime


class Item(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    time_added = models.DateField()
    last_edit = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name