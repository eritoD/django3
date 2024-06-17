from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnoUpdate', views.alumnoUpdate, name='alumnoUpdate'),
    
    path('ramo_form', views.ramo_form, name='ramo_form'),
    path('seccion_form', views.seccion_form, name='seccion_form'),

]