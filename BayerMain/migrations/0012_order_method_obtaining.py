# Generated by Django 5.1.2 on 2024-11-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0011_alter_order_payment_method_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method_obtaining',
            field=models.CharField(choices=[('selfcoll', 'Cамовызов'), ('delivery', 'Доставка')], default='selfcoll', max_length=50),
        ),
    ]