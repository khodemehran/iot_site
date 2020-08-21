from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Data(models.Model):

    humidity = models.FloatField(max_length=3)
    temp = models.FloatField(max_length=3)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tozih = models.CharField(max_length=300)




    def __str__(self):
        return self.tozih

    '''def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)'''




