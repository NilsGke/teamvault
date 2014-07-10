from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .views import live_search

urlpatterns = patterns('',
    url(
        r'^$',
        login_required(TemplateView.as_view(template_name="secrets/dashboard.html")),
        name='dashboard',
    ),
    url(
        r'^passwords/live-search$',
        live_search,
        name='secrets.live-search',
    ),
)
