from django.conf import settings
from products.models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __getitem__(self, key):
        return self.cart[key]

    def add(self, product_id, color_id, price, color, size):
        item = '{}-{}-{}'.format(product_id, color_id, size)
        if item not in self.cart:
            self.cart[item] = {'product_id': product_id, 'color_id': color_id, 'quantity': 1, 'price': price,
                               'color': color, 'size': size}
        else:
            self.cart[item]['quantity'] += 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        if item in self.cart:
            del self.cart[item]
            self.save()

    def update(self, item, quantity):
        self.cart[item]['quantity'] = quantity
        self.save()

    def __iter__(self):
        for item in self.cart.values():
            yield item

    def get_total_sum(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
