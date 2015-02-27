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



class masterbiketrails(models.Model):
    the_geom = models.LineStringField(srid=26915)
    objects = models.GeoManager()
