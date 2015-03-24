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
        if len(qs)>5:
            qs = qs[:5]
        json = {'name' +str(i):q.content_auto for i, q in enumerate(qs)}
        return HttpResponse(dumps(json),content_type="application/json")