from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('respForm', views.respForm, name='respForm'),
    path('details/<int:producto_id>', views.details, name='details'),
    path('nosotros', views.nosotros, name='nosotros'),
]