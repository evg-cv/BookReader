# Generated by Django 2.2.1 on 2019-05-05 09:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_borrow_favorite_reading'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
