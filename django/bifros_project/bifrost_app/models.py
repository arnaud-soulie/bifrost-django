from django.db import models

# Create your models here.
class Volume(models.Model):
    number=models.IntegerField(primary_key=True,unique=True)
    guest=models.CharField(max_length=40)
