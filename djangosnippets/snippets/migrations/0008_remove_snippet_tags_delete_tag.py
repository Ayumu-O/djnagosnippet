# Generated by Django 4.1.5 on 2023-01-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_alter_snippet_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
