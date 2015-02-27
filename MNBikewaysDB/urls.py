from django.conf.urls import patterns, include, url
from django.contrib import admin
from router.views import Routing

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MNBikewaysDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^route/', Routing.as_view()),
)
