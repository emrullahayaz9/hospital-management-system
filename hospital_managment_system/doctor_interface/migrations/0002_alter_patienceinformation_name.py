# Generated by Django 3.2.7 on 2023-07-25 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_interface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienceinformation',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
