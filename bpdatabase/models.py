from django.db import models
from django.utils import timezone

# Create your models here.
class myDb(models.Model):
    syst=models.IntegerField()
    diast=models.IntegerField()
    pred=models.CharField(max_length=30,default='-')
    date_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s - %s - %s"%(self.syst,self.diast,self.pred,self.date_time)

