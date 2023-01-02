# Generated by Django 4.1.5 on 2023-01-02 17:39

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('snippets', '0008_remove_snippet_tags_delete_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
    ]
