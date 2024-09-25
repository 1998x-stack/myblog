from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    title = models.CharField('标题', max_length=200)
    summary = models.TextField('摘要', blank=True)
    content = models.TextField('内容')
    tags = models.ManyToManyField('Tag', blank=True)  # 确保 tags 字段可以为空
    publish_date = models.DateTimeField('发布时间', auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.summary:
            self.summary = self.content[:200]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    visitor_id = models.CharField('游客ID', max_length=100, default='123')
    visitor_name = models.CharField('游客昵称', max_length=50, default='匿名用户')
    content = models.TextField('评论内容')
    publish_date = models.DateTimeField('评论时间', auto_now_add=True)

    def __str__(self):
        return f'{self.visitor_name}的评论'
