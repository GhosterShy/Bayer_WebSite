# Generated by Django 5.1.2 on 2024-11-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BayerMain', '0007_cartitem_sumtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=250000, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image_link1',
            field=models.ImageField(null=True, upload_to='static/img/categoryis'),
        ),
        migrations.AddField(
            model_name='category',
            name='image_link2',
            field=models.ImageField(null=True, upload_to='static/img/categoryis'),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='sumtotal',
            field=models.IntegerField(default=0.0),
        ),
    ]
