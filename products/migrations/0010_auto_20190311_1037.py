# Generated by Django 2.1.7 on 2019-03-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_footweartype_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footweartype',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='footwear_types/icons'),
        ),
    ]