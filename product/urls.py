from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(),name='product'),
    path('variants/<str:product>/', views.VariantView.as_view(),name='variants'),
    path('variants/', views.VariantView.as_view(),name='variants'),
    path('subvariants/', views.SubVariantView.as_view(),name='subvariants'),
    path('subvariants/<str:product>/', views.SubVariantView.as_view(),name='subvariants'),
    path('addstock/', views.AddStockView.as_view(),name='addstock'),
    path('removestock/', views.RemoveStockView.as_view(),name='removestock'),
]   