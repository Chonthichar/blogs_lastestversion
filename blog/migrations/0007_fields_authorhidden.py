# Generated by Django 4.2.7 on 2023-11-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_blog_fields_category_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='authorHidden',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
