# Generated by Django 2.2.1 on 2019-06-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0022_auto_20190619_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
