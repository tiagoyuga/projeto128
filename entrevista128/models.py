from django.db import models
from django.utils import timezone

class Modelo128(models.Model):
    campo1 = models.IntegerField()
    campo2 = models.TextField()
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.campo2
