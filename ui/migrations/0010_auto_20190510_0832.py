# Generated by Django 2.2.1 on 2019-05-10 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0009_waitinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reading.Book'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reading.Book'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reading.Book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reading.Book'),
        ),
        migrations.AlterField(
            model_name='waitinglist',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reading.Book'),
        ),
    ]
