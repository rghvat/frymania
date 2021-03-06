# Generated by Django 3.1.1 on 2021-06-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='on_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
