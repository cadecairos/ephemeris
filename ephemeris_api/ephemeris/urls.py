from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
