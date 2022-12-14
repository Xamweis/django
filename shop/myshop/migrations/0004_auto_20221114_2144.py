# Generated by Django 3.2.12 on 2022-11-14 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_alter_orders_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.articles'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.customers'),
        ),
    ]
