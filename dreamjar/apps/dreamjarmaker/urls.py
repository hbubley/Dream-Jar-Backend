from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.dreamjarmaker.views import DreamJarListCreateView, DreamJarDetailsView


urlpatterns = {
    url(r'^dreamjar/$', DreamJarListCreateView.as_view(), name='dreamjar'), 
    url(r'^dreamjar-update/(?P<pk>[0-9]+)/$', DreamJarDetailsView.as_view(), name='dreamjar-update'), 
}

urlpatterns = format_suffix_patterns(urlpatterns)