# Generated by Django 5.1.2 on 2024-12-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0020_alter_imageuser_image_alter_imageuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(default='Неизвестно', max_length=50, null=True),
        ),
    ]
