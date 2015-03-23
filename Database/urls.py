from django.conf.urls import patterns, include, url
from django.contrib import admin
from Data.views import MainPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Database.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainPage.as_view() ),
    url(r'^search/', include('haystack.urls') ),
)
