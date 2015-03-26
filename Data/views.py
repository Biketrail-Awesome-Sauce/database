from django.shortcuts import render
from django.views.generic import TemplateView
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point
from django.http import HttpResponse

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