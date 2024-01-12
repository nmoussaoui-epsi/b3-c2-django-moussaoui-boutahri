from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_sites, name='liste_sites'),
    path('ajouter/', views.ajouter_site, name='ajouter_site'),
    path('modifier/<int:site_id>/', views.modifier_site, name='modifier_site'),
    path('supprimer/<int:site_id>/', views.supprimer_site, name='supprimer_site'),
]
