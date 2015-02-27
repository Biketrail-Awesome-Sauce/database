from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from router.models import MinneapolisStreets




class Routing(View):

    def get(self,request,*args,**kwargs):
        lat1 = request.GET.get('lat1',42)
        lng1 = request.GET.get('lng1',-93)
        lat2 = request.GET.get('lat2',43)
        lng2 = request.GET.get('lng2', -92)

        where_now = MinneapolisStreets.objects.raw("select *,st_distance(the_geom,st_geomfromtext('POINT("+lat1 + " " + lng1+")',4326)) as dist from router_minneapolisstreets order by dist LIMIT 1;")
        print(where_now[0].the_geom)