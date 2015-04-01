__author__ = 'boyd'

from haystack import indexes

from Data.models import MinnesotaBikeTrails



class MinnesotaTrailsSearchable(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, model_attr='ccp_name')
    chicago_algorithm = indexes.FloatField(model_attr='rtng_cbf7')
    cyclopath_algorithm = indexes.FloatField(model_attr='rtng_ccpx')
    user_rating = indexes.FloatField(model_attr='rtng_mean')
    source = indexes.IntegerField(model_attr='source')
    target = indexes.IntegerField(model_attr='target')
    geometry = indexes.LocationField(model_attr='get_location')

    #for autocomplete
    content_auto = indexes.EdgeNgramField(model_attr='ccp_name')


    def get_model(self):
        return MinnesotaBikeTrails

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def __str__(self):
        return self.text