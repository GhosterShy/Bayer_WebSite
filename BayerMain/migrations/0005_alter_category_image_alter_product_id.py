# Generated by Django 5.1.2 on 2024-11-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0004_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/categoryis'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
