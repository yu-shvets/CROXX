from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .cart import Cart
from products.models import Product, Color
from django.views.generic import TemplateView
from django.http import JsonResponse
from .forms import OrderForm
from django.views.generic.edit import CreateView
from .models import Order, OrderItem


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        color = request.POST['color']
        color_id = Color.objects.filter(title=color).first().id
        if product.category.title == 'Jibbitz':
            size = None
        else:
            size = request.POST['size']
        cart.add(product_id, color_id, product.price, color, size)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class OrderView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        cart = Cart(self.request)
        cart_products = []
        for item in cart:
            product = Product.objects.get(id=int(item['product_id']))
            cart_products.append({'item_id': '{}-{}-{}'.format(item['product_id'], item['color_id'], item['size']),
                                  'product': product,
                                  'quantity': item['quantity'],
                                  'price': item['price'],
                                  'color': item['color'],
                                  'size': item['size'],
                                  'sum': item['quantity'] * item['price']})
        context['cart_products'] = cart_products
        context['order_form'] = OrderForm
        return context


def update_quantity(request, item_id):
    cart = Cart(request)
    price = cart[item_id]['price']
    response_data = {}
    if request.method == 'POST':
        new_quantity = int(request.POST['new_quantity'])
        cart.update(item_id, new_quantity)
        response_data['quantity'] = new_quantity
        response_data['sum'] = str(new_quantity * price) + ' UAH'
        print(response_data['sum'])
        response_data['cart_sum'] = str(cart.get_total_sum()) + ' UAH'
    return JsonResponse(response_data)


def cart_delete(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)
    return HttpResponseRedirect(reverse('order'))


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        self.obj = form.save(commit=False)
        self.obj.total_cost = cart.get_total_sum()
        self.obj.save()
        for item in cart:
            product = get_object_or_404(Product, id=int(item['product_id']))
            order_item = OrderItem(product=product, quantity=item['quantity'], price=item['price'], color=item['color'],
                                   size=item['size'], sum=item['quantity'] * item['price'], order=self.obj)
            order_item.save()
        cart.clear()
        return HttpResponseRedirect(reverse('success'))


class SuccessView(TemplateView):
    template_name = 'order_success.html'
