from django.db import models
from products.models import CommonInfo, Product


class Order(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    DELIVERY_CHOICES = (('Доставка Новой Почтой (50грн)', 'Доставка Новой Почтой (50грн)'),
                        ('Курьер по Киеву (20грн)', 'Курьер по Киеву (20грн)'))

    PAYMENT_CHOICES = (('При получении', 'При получении'),
                       ('Оплата на карту', 'Оплата на карту'))

    city = models.CharField(max_length=256)
    delivery_type = models.CharField(choices=DELIVERY_CHOICES, max_length=29, default='Доставка Новой Почтой')
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    patronymic = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=22)
    email = models.EmailField(blank=True, null=True)
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=15, default='Оплата на карту')
    np_branch = models.PositiveIntegerField(blank=True, null=True)
    total_cost = models.IntegerField()

    def __str__(self):
        return '#{} - {} {} - {}'.format(self.id, self.first_name, self.last_name, self.created)


class OrderItem(models.Model):

    class Meta(object):
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=256)
    size = models.CharField(max_length=256, blank=True, null=True)
    sum = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.product, self.order)
