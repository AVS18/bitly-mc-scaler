from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Url(models.Model):
    longurl = models.CharField(max_length=2048)
    shorturl = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    count = models.IntegerField()