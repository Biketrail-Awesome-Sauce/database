
from __future__ import unicode_literals

from django.contrib.gis.db import models


class BestBikeTrails(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ccp_name = models.CharField(max_length=80)
    gf_lyr_nom = models.CharField(max_length=80)
    one_way = models.IntegerField()
    rtng_mean = models.FloatField(blank=True, null=True)
    rtng_count = models.IntegerField(blank=True, null=True)
    rtng_cbf7 = models.FloatField()
    rtng_ccpx = models.FloatField(blank=True, null=True)
    item_tags = models.CharField(max_length=98)
    speedlimit = models.IntegerField(blank=True, null=True)
    lane_count = models.IntegerField(blank=True, null=True)
    out_ln_wid = models.IntegerField(blank=True, null=True)
    shld_width = models.IntegerField(blank=True, null=True)
    bike_facil = models.CharField(max_length=80)
    cautionary = models.CharField(max_length=80)
    cycleroute = models.CharField(max_length=80)
    ndl_elev = models.FloatField()
    ndr_elev = models.FloatField()
    source = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)
    cost = models.FloatField()
    the_geom = models.LineStringField()
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'Data_bestbiketrails'


class Bikeintersections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cnt = models.IntegerField(blank=True, null=True)
    chk = models.IntegerField(blank=True, null=True)
    ein = models.IntegerField(blank=True, null=True)
    eout = models.IntegerField(blank=True, null=True)
    the_geom = models.PointField(blank=True, null=True)
    name = models.CharField(max_length=130, blank=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'Data_bikeintersections'


class MinnesotaBikeTrails(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ccp_name = models.CharField(max_length=80)
    gf_lyr_nom = models.CharField(max_length=80)
    one_way = models.IntegerField()
    rtng_mean = models.FloatField(blank=True, null=True)
    rtng_count = models.IntegerField(blank=True, null=True)
    rtng_cbf7 = models.FloatField()
    rtng_ccpx = models.FloatField(blank=True, null=True)
    item_tags = models.CharField(max_length=98)
    speedlimit = models.IntegerField(blank=True, null=True)
    lane_count = models.IntegerField(blank=True, null=True)
    out_ln_wid = models.IntegerField(blank=True, null=True)
    shld_width = models.IntegerField(blank=True, null=True)
    bike_facil = models.CharField(max_length=80)
    cautionary = models.CharField(max_length=80)
    cycleroute = models.CharField(max_length=80)
    ndl_elev = models.FloatField()
    ndr_elev = models.FloatField()
    source = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)
    cost = models.FloatField()
    the_geom = models.LineStringField()
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'Data_minnesotabiketrails'



