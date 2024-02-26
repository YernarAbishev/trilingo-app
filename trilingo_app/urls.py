from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('class/themes/<slug:slug>/', views.themes_page, name='themes_page'),
    path('theme/detail/<slug:slug>/', views.theme_detail_page, name='theme_detail_page'),
    path('alphabets/kz/', views.alphabets_kz_page, name='alphabets_kz_page'),
    path('alphabets/ru/', views.alphabets_ru_page, name='alphabets_ru_page'),
    path('alphabets/en/', views.alphabets_en_page, name='alphabets_en_page'),
    path('filter/alphabet/kz/<slug:slug>/', views.filter_by_kz_page, name='filter_by_kz_page'),
    path('filter/alphabet/ru/<slug:slug>/', views.filter_by_ru_page, name='filter_by_ru_page'),
    path('filter/alphabet/en/<slug:slug>/', views.filter_by_en_page, name='filter_by_en_page'),
]