# Generated by Django 4.2.7 on 2023-12-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
