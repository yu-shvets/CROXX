# Generated by Django 2.1.7 on 2019-03-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190311_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='footweartype',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='footwear_types/icons'),
        ),
    ]
