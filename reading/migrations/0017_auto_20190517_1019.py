# Generated by Django 2.2.1 on 2019-05-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0016_auto_20190516_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='panjabi',
        ),
        migrations.AlterField(
            model_name='book',
            name='meta_data',
            field=models.ManyToManyField(blank=True, to='reading.MetaData'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='reading.Tag'),
        ),
    ]