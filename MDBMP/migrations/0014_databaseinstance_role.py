# Generated by Django 2.2 on 2019-05-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDBMP', '0013_server_rman_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseinstance',
            name='role',
            field=models.CharField(default='主实例', max_length=25),
            preserve_default=False,
        ),
    ]
