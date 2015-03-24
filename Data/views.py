from django.shortcuts import render
from django.views.generic import TemplateView
from haystack.query import SearchQuerySet
from django.http import HttpResponse
from json import dumps

class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')


class SearchAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        qs = SearchQuerySet().filter(content_auto=request.GET.get('q',""))
        json = {'name':q.content_auto for q in qs}
        return HttpResponse(dumps(json),content_type="application/json")