# Generated by Django 2.2 on 2019-05-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDBMP', '0002_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='ssh_port',
            field=models.IntegerField(default=22),
        ),
    ]
