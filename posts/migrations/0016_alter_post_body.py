# Generated by Django 4.0.5 on 2022-06-18 17:03

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]