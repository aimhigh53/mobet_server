# Generated by Django 3.0.5 on 2020-05-23 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobet_app', '0031_financeinfo_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrank',
            name='GRADE',
            field=models.CharField(default='C', max_length=5),
        ),
    ]
