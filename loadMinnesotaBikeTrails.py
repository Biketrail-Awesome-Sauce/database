__author__ = 'boyd'
from django.contrib.gis.utils import LayerMapping
from Data.models import MinnesotaBikeTrails,BestBikeTrails

mapping = {
    'ccp_name':'CCP_NAME',
    'gf_lyr_nom': 'gf_lyr_nom',
    'one_way' : 'one_way',
    'rtng_mean' : 'rtng_mean',
    'rtng_count' : 'rtng_count',
    'rtng_cbf7' : 'rtng_cbf7',
    'rtng_ccpx' : 'rtng_ccpx',
    'item_tags' : 'item_tags',
    'speedlimit' : 'speedlimit',
    'lane_count' : 'lane_count',
    'out_ln_wid' : 'out_ln_wid',
    'shld_width' : 'shld_width',
    'bike_facil' : 'bike_facil',
    'cautionary' : 'cautionary',
    'cycleroute' : 'cycleroute',
    'ndl_elev' : 'ndl_elev',
    'ndr_elev' : 'ndr_elev',
    'cost' : 'geom_len',

    'the_geom' : 'LINESTRING'

}
def run():
    lm = LayerMapping(BestBikeTrails,"cyclopath/best.shp",mapping=mapping)

    lm.save(verbose=True)