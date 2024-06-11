from django.urls import path
from . import views
urlpatterns=[
    path("", views.login, name='login'),
    path('index.html/', views.index, name='index'),
    path('asesorias.html/', views.asesorias, name='asesorias'),
    path('charlasOV.html/', views.charlasOV, name='charlasOV'),
    path('charts.html/', views.charts, name='charts'),
    path('defineTuFuturo.html/', views.defineTuFuturo, name='defineTuFuturo'),
    path('seguimientoCienciasBasicas.html/', views.seguimientoCienciasBasicas, name='seguimientoCienciasBasicas'),
    path('seguimientoNivelacion.html/', views.seguimientoNivelacion, name='seguimientoNivelacion'),
    path('tables.html/', views.tables, name='tables'),
    path('talleres.html/', views.talleres, name='talleres'),
    path('search.html/', views.search, name='search'),

]