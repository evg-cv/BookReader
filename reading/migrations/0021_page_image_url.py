# Generated by Django 2.2.1 on 2019-06-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0020_auto_20190617_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
