# Generated by Django 4.2.7 on 2023-11-05 12:17

# import ckeditor.fields
from django.db import migrations
from django.db.models import TextField


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_fields_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='content',
            field=TextField(blank=True, null=True),
        ),
    ]
