from django.db import models


class SmallData(models.Model):
    """
    dataset in use is dataset.xlsx
    """
    parameter = models.DecimalField()


class BigData(models.Model):
    """dataset in use is dataset-big.csv"""
    parameter = models.DecimalField()
