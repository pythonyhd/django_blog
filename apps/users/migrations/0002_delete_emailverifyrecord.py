# Generated by Django 2.2.6 on 2019-12-23 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailVerifyRecord',
        ),
    ]
