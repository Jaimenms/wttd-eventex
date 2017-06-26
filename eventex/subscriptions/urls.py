from django.conf.urls import include, url
from eventex.subscriptions.views import new, detail

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
]

