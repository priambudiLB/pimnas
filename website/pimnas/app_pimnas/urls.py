from django.conf.urls import url
from .views import index, signin, data_daerah, sponsor_departemen, sponsor_perusahaan, dokumen_proposal, dokumen_lpj, dokumen_lpjpublik

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^data-daerah/$', data_daerah, name='data_daerah'),
    url(r'^sponsor/departemen/$', sponsor_departemen, name='sponsor_departemen'),
    url(r'^sponsor/perusahaan/$', sponsor_perusahaan, name='sponsor_perusahaan'),
    url(r'^dokumen/proposal/$', dokumen_proposal, name='dokumen_proposal'),
    url(r'^dokumen/lpj/$', dokumen_lpj, name='dokumen_lpj'),
    url(r'^dokumen/lpj-publik/$', dokumen_lpjpublik, name='dokumen_lpjpublik'),
]