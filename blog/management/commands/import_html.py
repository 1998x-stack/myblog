# blog/management/commands/import_html.py

import os
from django.core.management.base import BaseCommand
from blog.models import Article
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Imports HTML files into the Article model'

    def add_arguments(self, parser):
        parser.add_argument('html_dir', type=str, help='Directory containing HTML files')

    def handle(self, *args, **kwargs):
        html_dir = kwargs['html_dir']

        # 检查目录是否存在
        if not os.path.exists(html_dir):
            self.stdout.write(self.style.ERROR(f'Directory not found: {html_dir}'))
            return

        # 使用 os.walk 递归遍历目录
        for root, dirs, files in os.walk(html_dir):
            for filename in files:
                if filename.endswith('.html'):
                    file_path = os.path.join(root, filename)
                    self.import_html_file(file_path, filename)

    # def import_html_file(self, file_path, filename):
    #     with open(file_path, 'r', encoding='utf-8') as file:
    #         content = file.read()

    #         # 使用文件名作为文章标题，去掉扩展名
    #         title = filename.replace('.html', '').replace('_', ' ').capitalize()

    #         # 创建并保存文章
    #         article = Article.objects.create(title=title, content=content)
    #         article.save()

    #         self.stdout.write(self.style.SUCCESS(f'Successfully imported: {filename}'))
    def import_html_file(self, file_path, filename):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # 使用 BeautifulSoup 提取 <title> 或 <h1> 标签的内容作为文章标题
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.title.string if soup.title else filename.replace('.html', '').replace('_', ' ').capitalize()

            # 创建并保存文章
            article = Article.objects.create(title=title, content=content)
            article.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully imported: {filename}'))