# Generated by Django 2.1.5 on 2019-04-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20190328_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='serveruser',
            name='require_trailing_slash',
            field=models.BooleanField(default=False),
        ),
    ]