# Generated by Django 4.1 on 2022-08-17 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_bid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'ordering': ['-amount']},
        ),
    ]
