from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('listing/', views.all_listings, name='all_listings'),
    path('add-listing/', views.add_listing, name='add_listing'),
    path('listing-confirm/', views.listing_confirm, name='listing_confirm'),
    path('about/', views.about_us, name='about_us'),
    path('premium/', views.premium, name='premium'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
] 