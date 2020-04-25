from django.db import models

# Create your models here.
class obj(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class sens(models.Model):
    name = models.CharField(max_length = 50)
    objfk = models.ForeignKey(obj, models.PROTECT)

    def __str__(self):
        return self.name

class values_sens(models.Model):
    tem = models.DecimalField(max_digits=11, decimal_places=4)
    dat = models.DateTimeField()
    sensfk = models.ForeignKey(sens, models.PROTECT)

    def __str__(self):
        return str(self.dat)
