from django.db import models

class DataSet(models.Model):
    data_name = models.CharField(max_length=100)
    row_size = models.IntegerField(default=0)
    column_size = models.IntegerField(default=0)
