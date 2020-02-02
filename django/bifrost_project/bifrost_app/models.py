from django.db import models

# Create your models here.
class Volume(models.Model):
    number=models.IntegerField(primary_key=True,unique=True)
    summary=models.TextField(blank=True)
    cover=models.ImageField(upload_to='cover_pics',blank=True)

    def __str__(self):
        return "Number : "+str(self.number)+" Summary : "+self.summary
