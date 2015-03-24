from django.shortcuts import render
from django.views.generic import TemplateView
from haystack.query import SearchQuerySet
from django.core import serializers
from django.http import HttpResponse

class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


class SearchAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        qs = SearchQuerySet().autocomplete(ccp_name=request.GET.get('q',""))[:5]
        json = serializers.serialize('json',qs)
        return HttpResponse(json)