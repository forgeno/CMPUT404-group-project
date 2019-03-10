# Generated by Django 2.1.5 on 2019-02-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contentType',
            field=models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], max_length=20),
        ),
        migrations.AlterField(
            model_name='follow',
            name='status',
            field=models.CharField(choices=[('FOLLOWING', 'FOLLOWING'), ('FRIENDS', 'FRIENDS'), ('DECLINED', 'DECLINED')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('text/markdown', 'text/markdown'), ('text/plain', 'text/plain'), ('application/base64', 'application/base64'), ('image/png;base64', 'image/png;base64'), ('image/jpeg;base64', 'image/jpeg;base64')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='visibility',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('FOAF', 'FOAF'), ('FRIENDS', 'FRIENDS'), ('PRIVATE', 'PRIVATE'), ('SERVERONLY', 'SERVERONLY')], max_length=10),
        ),
    ]