from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='login'),
    path('index.html/', views.index, name='index'),
    path('401.html/', views.e401, name='e401'),
    path('404.html/', views.e404, name='e404'),
    path('500.html/', views.charts, name='charts'),
    path('layoudsidenav.html/', views.layoudsidenav, name='layout_sidenav'),
    path('layoudstatic.html/', views.layoudstatic, name='layout_static'),
    path('password.html/', views.password, name='password'),
    path('register.html/', views.register, name='register'),
    path('tables.html/', views.tables, name='tables'),

]