from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^rend/$', views.rend, name='rend'),
    url(r'^get_name/$', views.get_name, name='get_name'),
 #url(r'^data3/$', views.data3, name='data3'),
 #url(r'^data2/$', views.data2, name='data2'),
#url(r'^test/$', views.test, name='test'),
#url(r'^gallery/$', views.gallery, name='gallery'),
]

