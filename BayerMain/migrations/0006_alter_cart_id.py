# Generated by Django 5.1.2 on 2024-11-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0005_alter_category_image_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]