# Generated by Django 4.1.5 on 2023-02-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item_descriptions',
            field=models.TextField(default='', max_length=1000),
        ),
    ]