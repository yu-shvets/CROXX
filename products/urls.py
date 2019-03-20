from django.urls import path, include
from .views import CatalogueListView, JibbitzCatalogueListView, ChildrenCatalogueListView, ProductDetailView

urlpatterns = [
    path('', CatalogueListView.as_view(), name='catalogue'),
    path('category/<category_slug>/', CatalogueListView.as_view(), name='catalogue_category'),
    path('brand/<brand_slug>/', CatalogueListView.as_view(), name='catalogue_brand'),
    path('footwear_type/<footwear_type_slug>/', CatalogueListView.as_view(), name='catalogue_footwear_type'),
    path('category/<category_slug>/brand/<brand_slug>/', CatalogueListView.as_view(), name='catalogue_category_brand'),
    path('category/<category_slug>/footwear_type/<footwear_type_slug>/', CatalogueListView.as_view(),
         name='catalogue_category_footwear_type'),
    path('category/<category_slug>/collection/<collection_slug>/', CatalogueListView.as_view(),
         name='catalogue_category_collection'),
    path('jibbitz/', JibbitzCatalogueListView.as_view(), name='catalogue_jibbitz'),
    path('children/', ChildrenCatalogueListView.as_view(), name='catalogue_children'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_info')
]
