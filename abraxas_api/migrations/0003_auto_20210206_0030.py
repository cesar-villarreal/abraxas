# Generated by Django 3.1.5 on 2021-02-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abraxas_api', '0002_auto_20210206_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
