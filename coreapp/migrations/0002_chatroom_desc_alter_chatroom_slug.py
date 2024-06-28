# Generated by Django 5.0.6 on 2024-06-26 07:43

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='desc',
            field=models.TextField(default='shfsjkf'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
