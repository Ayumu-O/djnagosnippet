# Generated by Django 4.1.4 on 2023-01-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='lang',
            field=models.CharField(default='text', max_length=128, verbose_name='言語'),
        ),
    ]
