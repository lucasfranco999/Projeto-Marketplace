# Generated by Django 4.2.2 on 2023-06-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_remove_doas_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='doas',
            name='desc',
            field=models.CharField(default='', max_length=200),
        ),
    ]