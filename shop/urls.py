from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.listing, name='products'),
    path('products/<int:pk>/', views.listing, name='products'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),

    path('search/', views.search, name='search'),
    path('send_message/', views.send_message_to_bot, name='send_message')
]
