from django.contrib.gis.db import models



class MinnesotaBikeTrails(models.Model):
    ccp_name = models.CharField(max_length=80)
    gf_lyr_nom = models.CharField(max_length=80)
    one_way = models.IntegerField()
    rtng_mean = models.FloatField()
    rtng_count = models.IntegerField()
    rtng_cbf7 = models.FloatField()
    rtng_ccpx = models.FloatField()
    item_tags = models.CharField(max_length=98)
    speedlimit = models.IntegerField()
    lane_count = models.IntegerField()
    out_ln_wid = models.IntegerField()
    shld_width = models.IntegerField()
    bike_facil = models.CharField(max_length=80)
    cautionary = models.CharField(max_length=80)
    cycleroute = models.CharField(max_length=80)
    ndl_elev = models.FloatField()
    ndr_elev = models.FloatField()
    #the next three need to be named as such because of pgRouting
    source = models.IntegerField(null=True)
    target = models.IntegerField(null=True)
    cost = models.FloatField()

    the_geom = models.LineStringField(srid=4326)
    objects = models.GeoManager()
