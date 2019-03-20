from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product
from .forms import CustomerEmailForm
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'index.html'


class CustomerEmailCreateView(CreateView):
    form_class = CustomerEmailForm
    success_url = '/#footer'


class CatalogueListView(ListView):
    model = Product
    template_name = 'catalogue.html'
    context_object_name = 'products'
    queryset = Product.objects.exclude(category__title='Jibbitz')
    paginate_by = 12

    def get_queryset(self):
        queryset = super(CatalogueListView, self).get_queryset()
        category = self.kwargs.get('category_slug')
        brand = self.kwargs.get('brand_slug')
        footwear_type = self.kwargs.get('footwear_type_slug')
        collection = self.kwargs.get('collection_slug')
        q = self.request.GET.get('query')
        if category:
            queryset = queryset.filter(category__slug=category)
        if brand:
            queryset = queryset.filter(brand__slug=brand)
        if footwear_type:
            queryset = queryset.filter(footwear_type__slug=footwear_type)
        if collection:
            queryset = queryset.filter(collection__slug=collection)
        if q:
            queryset = self.model.objects.filter(title__icontains=q.strip())
        return queryset


class JibbitzCatalogueListView(CatalogueListView):
    template_name = 'jibbitz.html'
    queryset = Product.objects.filter(category__title='Jibbitz')


class ChildrenCatalogueListView(CatalogueListView):
    def get_queryset(self):
        queryset = super(CatalogueListView, self).get_queryset()
        print(queryset)
        return queryset.filter(Q(category__title='Мальчикам') | Q(category__title='Девочкам'))


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'product'

