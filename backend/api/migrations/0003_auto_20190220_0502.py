# Generated by Django 2.1.5 on 2019-02-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190217_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowToView',
            fields=[
                ('user_id', models.CharField(max_length=1024, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='visibleTo',
            field=models.ManyToManyField(blank=True, related_name='posts', to='api.AllowToView'),
        ),
    ]
