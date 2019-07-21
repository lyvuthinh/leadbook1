from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact_filter, name='contact_filter'),
    path('<int:contact_id>/', views.contact_id_filter, name='contact_id_filter'),
]