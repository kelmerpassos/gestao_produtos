# Generated by Django 3.0.2 on 2020-01-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputlot',
            name='number_input',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='outputlot',
            name='number_output',
            field=models.IntegerField(unique=True),
        ),
    ]