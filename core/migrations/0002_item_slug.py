# Generated by Django 2.2.8 on 2020-06-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-item'),
            preserve_default=False,
        ),
    ]
