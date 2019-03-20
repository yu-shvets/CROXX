# Generated by Django 2.1.7 on 2019-03-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190319_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='sum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('Доставка Новой Почтой (50грн)', 'Доставка Новой Почтой (50грн)'), ('Курьер по Киеву (20грн)', 'Курьер по Киеву (20грн)')], default='Доставка Новой Почтой', max_length=29),
        ),
    ]
