from django.db import models

# Create your models here.
class TrainData(models.Model):
    description = models.CharField(max_length=250)
    recordDate = models.DateTimeField('date recorded')
    # etc....

class CnnModel(models.Model):
    description = models.CharField(max_length=250)
    last_trained = models.DateTimeField('last trained')
    epoke_count = models.IntegerField(default = 0)

# save me

