from products.models import FootwearType, Category, Brand, Collection
from products.forms import CustomerEmailForm
from cart.cart import Cart


def project_variables(request):
    footwear_types = FootwearType.objects.all()
    main_categories = Category.objects.all()
    brands = Brand.objects.all()
    collections = Collection.objects.all()
    email_form = CustomerEmailForm
    cart = Cart(request)
    cart_sum = cart.get_total_sum()
    return {'footwear_types': footwear_types, 'main_categories': main_categories, 'email_form': email_form,
            'brands': brands, 'collections': collections, 'cart_sum': cart_sum}

