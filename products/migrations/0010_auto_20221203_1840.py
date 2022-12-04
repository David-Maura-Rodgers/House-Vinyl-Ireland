# Generated by Django 3.2 on 2022-12-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20221129_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='stock_quantity',
        ),
        migrations.RemoveField(
            model_name='record',
            name='track_list',
        ),
        migrations.AddField(
            model_name='record',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]