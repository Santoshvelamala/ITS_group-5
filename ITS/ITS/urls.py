from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from jaikissan import views


urlpatterns = [
    url(r'^$', views.rend, name='rend'),
    url(r'^admin/', admin.site.urls),
    url(r'^jaikissan/', views.index, name='index'),
    url(r'^kissans/', views.KissanList.as_view()),
    url(r'^kissans/(?P<pk>[0-9]+)/$', views.KissanDetail.as_view()),
    url(r'^farms/', views.FarmList.as_view()),
    url(r'^farms/(?P<pk>[0-9]+)/$', views.FarmDetail.as_view()),
    url(r'^wells/', views.WellList.as_view()),
    url(r'^wells/(?P<pk>[0-9]+)/$', views.WellDetail.as_view()),
    url(r'^wellupdates/', views.WellUpdateList.as_view()),
    url(r'^wellupdates/(?P<pk>[0-9]+)/$', views.WellUpdateDetail.as_view()),
    url(r'^familymembers/', views.FamilyMemberList.as_view()),
    url(r'^familymembers/(?P<pk>[0-9]+)/$', views.FamilyMemberDetail.as_view()),
    url(r'^questions/', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
    url(r'^answers/', views.AnswerList.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view()),
    url(r'^seeds/', views.SeedList.as_view()),
    url(r'^seeds/(?P<pk>[0-9]+)/$', views.SeedDetail.as_view()),
    url(r'^fertilizers/', views.FertilizerList.as_view()),
    url(r'^fertilizers/(?P<pk>[0-9]+)/$', views.FertilizerDetail.as_view()),
    url(r'^cropprices/', views.CropPriceList.as_view()),
    url(r'^cropprices/(?P<pk>[0-9]+)/$', views.CropPriceDetail.as_view()),
    url(r'^houses/', views.HouseList.as_view()),
    url(r'^houses/(?P<pk>[0-9]+)/$', views.HouseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
