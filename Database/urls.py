from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from Data.views import MainPage, SearchAjax, GeoJsonAjax

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Database.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainPage.as_view() ),
    url(r'^searchAjax/', csrf_exempt(SearchAjax.as_view()) ),
    url(r'^geoJson/',csrf_exempt(GeoJsonAjax.as_view()))
)
