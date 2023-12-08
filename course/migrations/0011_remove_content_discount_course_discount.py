# Generated by Django 4.2.7 on 2023-12-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='discount',
        ),
        migrations.AddField(
            model_name='course',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=4, null=True),
        ),
    ]