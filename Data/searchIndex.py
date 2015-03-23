__author__ = 'boyd'

from haystack import indexes

from Data.models import MinnesotaBikeTrails



class MinnesotaTrailsSearchable(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, template=True, model_attr='ccp_name')
    chicago_algorithm = indexes.FloatField(model_attr='rtng_cbf7')
    cyclopath_algorithm = indexes.FloatField(model_attr='rtng_ccpx')
    user_rating = indexes.FloatField(model_attr='rtng_mean')
    geometry = indexes.LocationField(model_attr='the_geom')

    #for autocomplete
    content_auto = indexes.EdgeNgramField(model_attr='content')

    def get_model(self):
        return MinnesotaBikeTrails

    def __str__(self):
        return self.text