# Generated by Django 3.2 on 2022-10-05 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
                ('friendly_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('artist', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField(blank=True, null=True)),
                ('stock_quantity', models.IntegerField(default=1)),
                ('track_list', models.TextField()),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.label')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_name', models.CharField(blank=True, max_length=254, null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.record')),
            ],
        ),
    ]