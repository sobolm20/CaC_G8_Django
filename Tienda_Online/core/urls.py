from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('details/<int:producto_id>/', views.details, name='details')
]
