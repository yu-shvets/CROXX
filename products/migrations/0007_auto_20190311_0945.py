# Generated by Django 2.1.7 on 2019-03-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190306_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title_image',
            field=models.ImageField(upload_to='items/title_images'),
        ),
    ]
