# Generated by Django 2.0.1 on 2018-01-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20180130_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
