from django.contrib.gis.db import models



class MinnesotaBikeTrails(models.Model):
    ccp_name = models.CharField(max_length=80,blank=True)
    gf_lyr_nom = models.CharField(max_length=80)
    one_way = models.IntegerField()
    rtng_mean = models.FloatField(null=True)
    rtng_count = models.IntegerField(null=True)
    rtng_cbf7 = models.FloatField()
    rtng_ccpx = models.FloatField(null=True)
    item_tags = models.CharField(max_length=98,blank=True)
    speedlimit = models.IntegerField(null=True)
    lane_count = models.IntegerField(null=True)
    out_ln_wid = models.IntegerField(null=True)
    shld_width = models.IntegerField(null=True)
    bike_facil = models.CharField(max_length=80,blank=True)
    cautionary = models.CharField(max_length=80,blank=True)
    cycleroute = models.CharField(max_length=80,blank=True)
    ndl_elev = models.FloatField()
    ndr_elev = models.FloatField()
    #the next three need to be named as such because of pgRouting
    source = models.IntegerField(null=True)
    target = models.IntegerField(null=True)
    cost = models.FloatField()

    the_geom = models.LineStringField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.ccp_name
