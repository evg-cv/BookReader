# Generated by Django 2.2.1 on 2019-05-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
