# Generated by Django 4.0.5 on 2022-06-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
