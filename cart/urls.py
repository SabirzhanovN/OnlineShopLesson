from django.urls import path

from . import views

urlpatterns = [
    path('add_to_favorites/<int:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:pk>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', views.favorites_list, name='favorites'),

    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_list/', views.cart_list, name='cart_list'),
    path('remove_cart/<int:pk>/', views.remove_cart, name='remove_cart'),
    path('remove_all_cart/', views.remove_all_cart, name='remove_all_cart'),

]

