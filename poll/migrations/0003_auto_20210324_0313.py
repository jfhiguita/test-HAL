# Generated by Django 3.1.7 on 2021-03-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20210324_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='response',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
