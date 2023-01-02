from django.db import models
from django.conf import settings

from taggit_selectize.managers import TaggableManager

# Create your models here.

class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=128)
    code = models.TextField('コード', blank=True)
    lang = models.CharField('言語', default="text", max_length=128, null=True, blank=True)
    description = models.TextField('説明', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="snippets",
        verbose_name='投稿者',
        on_delete=models.CASCADE)
    tags = TaggableManager(verbose_name='タグ')
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    class Meta():
        db_table = 'snippets'

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField('コメント')
    to = models.ForeignKey(
        Snippet,
        related_name="comments",
        verbose_name='スニペット',
        on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        verbose_name='投稿者',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)

    class Meta():
        db_table = 'comments'

    def __str__(self):
        return self.content
