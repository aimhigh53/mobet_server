# Generated by Django 3.0.5 on 2020-05-14 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobet_app', '0010_remove_notification_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='USER_ID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user', to='mobet_app.User'),
            preserve_default=False,
        ),
    ]
