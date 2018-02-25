from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.university_and_specialty_lists, name='university_and_specialty_lists'),
    url(r'^specialties/$', views.specialty_list, name='specialty_list'),
    url(r'^specialty/(?P<pk>\d+)/$', views.specialty_detail, name='specialty_detail'),
    url(r'^universities/$', views.university_list, name='university_list'),
    url(r'^university/(?P<pk>\d+)/$', views.university_detail, name='university_detail'),
    url(r'^search_form/$', views.subjects_and_scores_search_form, name='subjects_and_scores_search_form'),
    url(r'^search/$', views.subjects_and_scores_search, name='subjects_and_scores_search')
]