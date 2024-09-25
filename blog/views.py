from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Tag, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from haystack.query import SearchQuerySet
from .forms import CommentForm, ArticleForm
import uuid

def article_list(request):
    tag_name = request.GET.get('tag')
    per_page = request.GET.get('per_page', 5)
    try:
        per_page = int(per_page)
        if per_page not in [5, 10, 20]:
            per_page = 5
    except ValueError:
        per_page = 5

    if tag_name:
        articles = Article.objects.filter(tags__name=tag_name).order_by('-publish_date')
    else:
        articles = Article.objects.all().order_by('-publish_date')
    
    paginator = Paginator(articles, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    return render(request, 'blog/article_list.html', {'page_obj': page_obj, 'tags': tags})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all().order_by('-publish_date')
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments})

def search(request):
    query = request.GET.get('q', '')
    if query:
        articles = SearchQuerySet().filter(content=query).order_by('-publish_date')
    else:
        articles = SearchQuerySet().all().order_by('-publish_date')

    per_page = request.GET.get('per_page', 5)
    paginator = Paginator(articles, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'page_obj': page_obj, 'query': query})

def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            visitor_id = request.session.get('visitor_id')
            if not visitor_id:
                visitor_id = str(uuid.uuid4())
                request.session['visitor_id'] = visitor_id
            visitor_name = f"Visitor{str(visitor_id)[-5:]}"
            Comment.objects.create(
                article=article,
                visitor_id=visitor_id,
                visitor_name=visitor_name,
                content=content
            )
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'article': article})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # 提交成功后重定向至文章列表页
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})


def search(request):
    query = request.GET.get('q', '')
    results = SearchQuerySet().filter(content=query)  # 使用 Haystack 搜索

    # 分页设置
    paginator = Paginator(results, 10)  # 每页显示 10 条结果
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/search_results.html', {
        'query': query,
        'results': page_obj
    })