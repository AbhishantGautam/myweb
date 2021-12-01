# Generated by Django 3.2.8 on 2021-10-22 16:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_rename_topic_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topics',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
