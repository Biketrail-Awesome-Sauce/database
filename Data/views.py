from django.shortcuts import render
from django.views.generic import TemplateView, View
from haystack.query import SearchQuerySet
from haystack.utils.geo import Point
from django.http import HttpResponse
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from django.db import connection

from Data.models import BestBikeTrails, MinnesotaBikeTrails

from requests import get
import xml.etree.ElementTree as ET
from json import dumps, loads


class MainPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class SearchAjax(TemplateView):
    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat',''))
        lng = float(request.GET.get('lng',''))
        qs = SearchQuerySet().filter(content_auto=request.GET.get('q',"")).distance('geometry',Point(lng,lat,srid=4326)).order_by('distance')
        if len(qs)>6:
            qs = qs[:5]
        json = [(q.content_auto," "+("%.2f" % (q.distance.m if q.distance.m<1000 else q.distance.mi))+(" meters" if q.distance.m<1000 else " miles"),q.source,q.target,GEOSGeometry(q.geometry).coords[1], GEOSGeometry(q.geometry).coords[0]) for q in qs]
        return HttpResponse(dumps(json),content_type="application/json")



class GeoJsonAjax(View):
    def get(self,request, *args, **kwargs):
        lat = float(request.GET.get('lat1','45'))
        lng = float(request.GET.get('lng1','-93.265'))
        qs = BestBikeTrails.objects.filter(the_geom__distance_lte=(Point(lng,lat,srid=4326),D(mi=2)))
        gj = []
        for item in qs:
            poly = loads(GEOSGeometry(item.the_geom,srid=4326).geojson)
            poly['properties'] = {'name': item.ccp_name}
            gj.append(poly)
        return HttpResponse(dumps(gj),content_type="application/json")


class RouterAjax(View):
    def get(self, request, *args, **kwargs):
        id1 =  request.GET.get('bid')
        id2 = request.GET.get('eid')
        sql_inside_of_function = "select id, source, target, cost * (4-rtng_ccpx) * (4-rtng_mean) * (4-rtng_cbf7)+case when one_way=-1 then 1000000 else 0 END as cost,cost * (4-rtng_ccpx)*(4-rtng_mean)*(4-rtng_cbf7) + case when one_way=1 then 1000000 else 0 END as reverse_cost from \"Data_minnesotabiketrails\"\'"
        sql_function = "select ccp_name, the_geom, bt.cost from pgr_dijkstra(\'"

        cursor = connection.cursor()
        cursor.execute(sql_function+sql_inside_of_function+", %s , %s , true,true) join \"Data_minnesotabiketrails\" as bt on bt.id=id2",(str(id1),str(id2),))
        all = cursor.fetchall()
        names = []
        gj = []
        for item in all:
            names.append((item[0],item[2]))
            poly = loads(GEOSGeometry(item[1]).geojson)
            poly['properties'] = {'name':item[0]}
            gj.append(poly)
        #next is getting the distance on each same named trail section
        previous_name = 'as;dknfiowienfkdoasndf' #needs to be something it won't be; it could be empty string
        sent_names = []
        dist_on_path = 0
        for i,n in enumerate(names):
            if i==0:
                previous_name=n[0]
            if n[0]==previous_name:
                dist_on_path +=n[1]
            else:
                sent_names.append((previous_name,"%.2f" % dist_on_path))
                dist_on_path=n[1]
                previous_name = n[0]
            if i==len(names)-1:
                    sent_names.append((previous_name, "%.2f" % dist_on_path))

        return HttpResponse(dumps({'names':sent_names, 'geojson':gj}), content_type="application/json; charset='utf-8'")


class NiceRideAjax(View):
    def get(self, request, *args, **kwargs):
        r = get(url="https://secure.niceridemn.org/data2/bikeStations.xml")
        doc = ET.fromstring(r.text)
        stations = doc.findall('station')
        # this isn't really json it is a bunch of  python dicts inside a python list
        json = [{item.tag: item.text for item in station} for station in stations]  #look at that beauty there
        gj = []
        for d in json:
            if d['public']=='true':
                lat = d['lat']
                long = d['long']
                del d['lat']
                del d['long']
                gj.append({'type': 'Point', 'coordinates': [long, lat], 'properties': d})
        return HttpResponse(dumps(gj), content_type="application/json; charset='utf-8'")
