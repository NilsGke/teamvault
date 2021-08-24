from django.conf.urls import url

from .api import SecretDetail, SecretList, SecretRevisionDetail, data_get


urlpatterns = (
    url(
        r'^secrets/$',
        SecretList.as_view(),
        name='api.secret_list',
    ),
    url(
        r'^secrets/(?P<hashid>\w+)/$',
        SecretDetail.as_view(),
        name='api.secret_detail',
    ),
    url(
        r'^secret-revisions/(?P<hashid>\w+)/$',
        SecretRevisionDetail.as_view(),
        name='api.secret-revision_detail',
    ),
    url(
        r'^secret-revisions/(?P<hashid>\w+)/data$',
        data_get,
        name='api.secret-revision_data',
    ),
)
