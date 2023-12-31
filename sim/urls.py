from django.urls import path

from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('search/', views.search_view, name='search_view'),
    path('search/results/', views.search_results_view, name='search_results_view'),
    path('example/', views.example, name='example'),
    path('sample-post/', views.sample_post, name='sample-post'),
    path('contact-form/', views.contact_form, name='contact_form'),
]
