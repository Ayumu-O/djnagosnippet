# Generated by Django 4.1.4 on 2023-01-02 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0003_alter_snippet_lang'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='snippet',
            table='snippets',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='コメント')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.snippet', verbose_name='スニペット')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]