import django
from router.models import MasterBikeTrails
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping

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
    'objectid' : 'OBJECTID',
    'active' : 'ACTIVE',
    'notes' : 'NOTES',
    'name' : 'NAME',
    'width' : 'WIDTH',
    'grade' : 'GRADE',
    'lighted' : 'LIGHTED',
    'operation' : 'OPPERATION',
    'proposed' : 'PROPOSED',
    'road_name' : "ROAD_NAME",
    'road_speed' : "ROAD_SPEED",
    'lane_numb' : "LANE_NUMB",
    'lane_width' : "LANE_WIDTH",
    'lane_dir' : "LANE_DIR",
    'lane_type' : 'LANE_TYPE',
    'cost' : 'SHAPE_LENG',
    'maintainer' : 'MAINTAINER',
    'surf_type' : "SURF_TYPE",
    "surf_qual" : "SURF_QAUL",
    'the_geom' : 'LINESTRING'}

def run():
    lm = LayerMapping(MasterBikeTrails,DataSource("9CountyMetro/Bikeways.shp"),map9CountyMetro)
    lm.save(verbose=False,step=1000,progress=True)


if __name__=='__main__':
    run()