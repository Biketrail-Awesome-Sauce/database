from django.contrib.gis.db import models


# Here is the Hennepin County Street Centerlines table

#the shapefile has EPSG:26915 crs
class HennepinStreets(models.Model):
    object_id = models.IntegerField()
    street_name = models.CharField(max_length=83)
    cost = models.FloatField()
    join_id = models.IntegerField()

    source = models.IntegerField(null=True,blank=True)
    target = models.IntegerField(null=True,blank=True)

    the_geom = models.LineStringField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.street_name, str(self.cost))


class MinneapolisStreets(models.Model):
    object_id = models.FloatField()
    street_name = models.CharField(max_length=35)
    speed_lim = models.IntegerField()
    oneway = models.CharField(max_length=2)
    cost = models.FloatField()

    source = models.IntegerField(null=True, blank=True)
    target = models.IntegerField(null=True,blank=True)

    the_geom = models.LineStringField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.street_name, str(self.cost))



class MasterBikeTrails(models.Model):
    objectid = models.IntegerField(blank=True,null=True)
    active = models.IntegerField(blank=True,null=True)
    notes = models.CharField(max_length=250,blank=True)
    name = models.CharField(max_length=50,blank=True)
    width = models.IntegerField(null=True,blank=True)
    grade = models.CharField(max_length=1,blank=True)
    lighted = models.CharField(max_length=1,blank=True)
    operation = models.CharField(max_length=50,blank=True)
    proposed = models.CharField(max_length=1,blank=True)
    road_name = models.CharField(max_length=35,blank=True)
    road_speed = models.IntegerField(blank=True,null=True)
    lane_numb = models.IntegerField(blank=True,null=True)
    lane_width = models.IntegerField(blank=True,null=True)
    lane_dir = models.CharField(max_length=10,blank=True)
    lane_type = models.CharField(max_length=2,blank=True)
    cost = models.FloatField(null=True,blank=True)
    maintainer = models.CharField(max_length=35,blank=True)
    surf_type = models.CharField(max_length=25,blank=True)
    surf_qual = models.CharField(max_length=25,blank=True)
    the_geom = models.LineStringField(srid=26915,null=True,blank=True)
    objects = models.GeoManager()

    def __str__(self):
        return "On {0} for {1} meters".format(self.name, str(self.cost))