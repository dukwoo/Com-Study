# Generated by Django 4.0.6 on 2022-08-22 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='diary/images/%Y/%m/%d/'),
        ),
    ]
