# Generated by Django 4.0.5 on 2022-07-27 06:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
