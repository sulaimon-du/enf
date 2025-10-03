from django.urls import path
from . import views

app_name= 'base'

urlpatterns = [
    path('', views.Index.as_view(), name='catalog_all'),
    path('catalog/', views.CatalogView.as_view(), name='all_catalog'),
    path('catalog/<slug:category_slug>/', views.CatalogView().as_view(), name='catalog'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='product_detail'),
]
