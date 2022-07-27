# Generated by Django 3.2.7 on 2021-09-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210907_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]