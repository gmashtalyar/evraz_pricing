from django.db import models


class MarketingData(models.Model):
    A = models.IntegerField()
    B = models.IntegerField()
    C = models.IntegerField()
    Price = models.IntegerField()


class MarketingData2(models.Model):
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()


class MarketingData3(models.Model):
    name = models.CharField(max_length=50)
    width = models.IntegerField()
    length = models.IntegerField()
    height = models.IntegerField()
    price = models.IntegerField()
    frame_type = models.CharField(max_length=3)
    roof_type = models.CharField(max_length=25)
    wall_type = models.CharField(max_length=25)
    roof_panels = models.CharField(max_length=25)
    wall_panels = models.CharField(max_length=25)
    membrane = models.CharField(max_length=25)
    snow = models.CharField(max_length=3)
    wind = models.CharField(max_length=3)

