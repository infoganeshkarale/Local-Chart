from django.db import models


# Create your models here.
class PMSData(models.Model):
    status = models.CharField(max_length=100)
    work = models.IntegerField()

    class Meta:
        verbose_name_plural = 'PMS Analytics Data'

    def __str__(self):
        return f'{self.status}-{self.work}'
