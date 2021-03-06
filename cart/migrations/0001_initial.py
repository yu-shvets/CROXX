# Generated by Django 2.1.7 on 2019-03-19 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0013_auto_20190314_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=256)),
                ('delivery_type', models.CharField(choices=[('Доставка Новой Почтой', 'Доставка Новой Почтой'), ('Курьер по Киеву', 'Курьер по Киеву')], default='Доставка Новой Почтой', max_length=21)),
                ('first_name', models.CharField(max_length=256)),
                ('second_name', models.CharField(max_length=256)),
                ('patronymic', models.CharField(blank=True, max_length=256, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('payment_type', models.CharField(choices=[('При получении', 'При получении'), ('Оплата на карту', 'Оплата на карту')], default='Оплата на карту', max_length=15)),
                ('np_branch', models.PositiveIntegerField(blank=True, null=True)),
                ('total_cost', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=256)),
                ('size', models.CharField(blank=True, max_length=256, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
    ]
