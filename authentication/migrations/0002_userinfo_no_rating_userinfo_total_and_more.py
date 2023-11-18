# Generated by Django 4.2.7 on 2023-11-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='no_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='total',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
