# Generated by Django 5.1.2 on 2024-11-19 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0013_orderitem_seller_alter_order_method_obtaining_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='seller',
        ),
    ]
