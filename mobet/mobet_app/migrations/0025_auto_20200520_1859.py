# Generated by Django 3.0.5 on 2020-05-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobet_app', '0024_competitionset_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeinfo',
            name='PAYMENTTIME',
            field=models.DateTimeField(),
        ),
    ]
