# blog/search_indexes.py

from haystack import indexes
from .models import Article
from django.utils import timezone

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    # 定义主索引字段，使用模板进行灵活配置
    text = indexes.CharField(document=True, use_template=True)
    
    # 额外定义的可索引字段
    title = indexes.CharField(model_attr='title')  # 直接索引 title 字段
    summary = indexes.CharField(model_attr='summary', null=True)  # 直接索引 summary 字段
    content = indexes.CharField(model_attr='content')  # 直接索引 content 字段
    publish_date = indexes.DateTimeField(model_attr='publish_date')  # 索引发布时间
    
    # 索引标签字段
    tags = indexes.CharField()

    def get_model(self):
        return Article

    def prepare_tags(self, obj):
        """将 tags 转换为逗号分隔的字符串进行索引"""
        return ', '.join([tag.name for tag in obj.tags.all()])

    def index_queryset(self, using=None):
        # 返回你希望被索引的对象的查询集，这里仅索引发布过的文章
        return self.get_model().objects.filter(publish_date__lte=timezone.now())
