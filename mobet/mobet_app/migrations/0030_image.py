# Generated by Django 3.0.5 on 2020-05-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobet_app', '0029_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='usr')),
            ],
        ),
    ]