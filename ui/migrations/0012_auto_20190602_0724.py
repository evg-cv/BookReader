# Generated by Django 2.2.1 on 2019-06-02 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0018_book_created_at'),
        ('ui', '0011_auto_20190529_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='annotation',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='title',
        ),
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reading.Category'),
            preserve_default=False,
        ),
    ]
