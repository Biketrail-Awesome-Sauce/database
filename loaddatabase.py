import django
from router.models import masterbiketrails
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping
from databaseloader import masterbiketrails_mapping
django.setup()

mapping = {'object_id':'OBJECTID',
            'street_name':'ST_NAME',
           'cost': 'Shapelen',
           'join_id':'JOIN_ID',
           'the_geom':'LINESTRING'}

mapMinneapolis = {'object_id':'GBSID',
            'street_name':'STREETNAME',
           'cost': 'SHAPE_LEN',
           'speed_lim':'SPEED_LIM',
           'the_geom':'LINESTRING',
            'oneway':'ONEWAY'}

map9CountyMetro = {
    'the_geom' : 'LINESTRING'}

def run():
    lm = LayerMapping(masterbiketrails, DataSource("9CountyMetro/Bikeways.shp"),map9CountyMetro)
    lm.save(verbose=False,step=1000,progress=True)


if __name__=='__main__':
    run()