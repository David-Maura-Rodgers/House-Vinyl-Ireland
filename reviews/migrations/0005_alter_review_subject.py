# Generated by Django 3.2 on 2022-12-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='subject',
            field=models.CharField(default='Enter Review Title', max_length=100),
        ),
    ]
