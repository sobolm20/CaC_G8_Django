from django.urls import path
from gerencia import views

urlpatterns = [
    path('', views.index_gerencia, name='inicio_gerencia'),
    path('gerencia/proovedor', views.index_gerencia, name=''),

]