# Generated by Django 3.2 on 2022-12-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_original_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
    ]
