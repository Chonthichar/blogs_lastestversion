# Generated by Django 4.2.7 on 2023-11-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_rename_text_add_comment_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]