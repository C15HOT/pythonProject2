from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('regions/', views.Regions.as_view(), name='regions'),
    path('advertisements', AdvertisementListView.as_view(), name='advertisement' ),
    path('advertisements/<int:pk>',AdvertisementDetailView.as_view(), name='advertisements-detail'),


]