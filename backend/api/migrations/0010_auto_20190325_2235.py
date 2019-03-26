# Generated by Django 2.1.5 on 2019-03-25 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_serveruser_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='serveruser',
            name='send_password',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serveruser',
            name='send_username',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]