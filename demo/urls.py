# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views
from .views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView

#app_name = 'demo'

urlpatterns = [
#    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
#demo pgm 	
    url(r'^$', views.findsth_home, name='findsth_home'),	
    url(r'^fhome$', views.findsth_home, name='findsth_home'),	
    url(r'^fsearch$', views.findsth_search, name='findsth_search'),
    url(r'^fmap/(?P<pk>\w+)$', views.findsth_map, name='findsth_map'),
]
