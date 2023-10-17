from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('contact2', views.contact2, name='contact2'),
    path('details/<int:producto_id>', views.details, name='details'),
]
