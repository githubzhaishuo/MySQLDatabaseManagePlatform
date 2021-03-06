# Generated by Django 2.2 on 2019-05-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDBMP', '0017_sqlaudit_reasons_for_failure'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('run_time', models.CharField(max_length=50, null=True)),
                ('cpu_load', models.DecimalField(decimal_places=2, max_digits=10)),
                ('free_used', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
