from django.db import models


class SmallData(models.Model):
    """
    dataset in use is dataset.xlsx
    """
    parameter = models.DecimalField(decimal_places=4, max_digits=10)


class BigData(models.Model):
    """dataset in use is dataset-big.csv"""
    parameter = models.DecimalField(decimal_places=4, max_digits=10)
