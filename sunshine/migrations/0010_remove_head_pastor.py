# Generated by Django 2.0 on 2019-11-13 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0009_head_pastor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='head',
            name='pastor',
        ),
    ]