from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search_view, name='search_view'),
    path('search/results/', views.search_results_view, name='search_results_view'),
    path('example/', views.example, name='example'),
    path('sample-post/', views.sample_post, name='sample-post'),
]
