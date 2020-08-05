from django.db import models

# Create your models here.
class Data(models.Model):

    rotobat = models.FloatField(max_length=3)
    dama = models.FloatField(max_length=3)
    date = models.DateTimeField()
    tozih = models.CharField(max_length=300)
    


