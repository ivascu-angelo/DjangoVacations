# Generated by Django 4.2.9 on 2024-03-05 03:58

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitetoteam',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invitetoteam',
            name='token',
            field=models.CharField(default=django.utils.crypto.get_random_string, max_length=20, unique=True),
        ),
    ]