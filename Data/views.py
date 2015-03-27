from django.shortcuts import render
from django.views.generic import TemplateView, View
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point
from django.http import HttpResponse
from django.contrib.gis.measure import D
from django.core import serializers
from Data.models import MinnesotaBikeTrails


from json import dumps

class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


class SearchAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        qs = SearchQuerySet().filter(content_auto=request.GET.get('q',"")).distance('geometry',Point(-93.265,45,srid=4326)).order_by('distance')
        if len(qs)>6:
            qs = qs[:5]
        json = [(q.content_auto," "+str(q.distance.m)+" meters") for q in qs]
        return HttpResponse(dumps(json),content_type="application/json")



class GeoJsonAjax(View):
    def get(self,request, *args, **kwargs):
        qs = MinnesotaBikeTrails.objects.filter(the_geom__distance_lte=(Point(request.GET.get('lng1','-93.265')),D(mi=2)))
        geoJson = serializers.serialize('json',qs)
        return HttpResponse(geoJson,content_type="application/json")