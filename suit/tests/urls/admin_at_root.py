from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns =[
    # Examples for custom menu
    url(r'^', include(admin.site.urls)),
]
