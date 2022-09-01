from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.product_create_view),
    path('list_create/', views.product_list_create_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]