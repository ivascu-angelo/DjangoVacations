# Generated by Django 4.2.9 on 2024-02-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0002_alter_vacation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
