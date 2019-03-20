from django.contrib import admin
from .models import SpecsType, Specification, Product, Image, Category, FootwearType, Brand, Collection, CustomerEmail, \
    Color, Size



class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 0


@admin.register(SpecsType)
class SpecsTypeAdmin(admin.ModelAdmin):
    inlines = (SpecificationInline,)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


admin.site.register(Category)
admin.site.register(FootwearType)
admin.site.register(Brand)
admin.site.register(Collection)
admin.site.register(CustomerEmail)
admin.site.register(Color)
admin.site.register(Size)
