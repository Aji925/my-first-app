# Generated by Django 2.2.5 on 2019-10-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190930_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_img'),
        ),
    ]
