# Create your models here.
from django.db import models

# Create history models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    result = models.CharField(blank=False, null=False, max_length=200)
    confidence = models.FloatField(blank=False, null=False, default=0.0)
    sequence = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.title + self.result + str(self.date) + self.user.username + str(self.confidence) + self.sequence 



    

