# blog/management/commands/import_markdown.py

import os
from django.core.management.base import BaseCommand
from blog.models import Article

class Command(BaseCommand):
    help = 'Imports markdown files into the Article model'

    def add_arguments(self, parser):
        parser.add_argument('markdown_dir', type=str, help='Directory containing markdown files')

    def handle(self, *args, **kwargs):
        markdown_dir = kwargs['markdown_dir']

        # 检查目录是否存在
        if not os.path.exists(markdown_dir):
            self.stdout.write(self.style.ERROR(f'Directory not found: {markdown_dir}'))
            return

        # 使用 os.walk 递归遍历目录
        for root, dirs, files in os.walk(markdown_dir):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = os.path.join(root, filename)
                    self.import_markdown_file(file_path, filename)

    def import_markdown_file(self, file_path, filename):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # 使用文件名作为文章标题，去掉扩展名
            title = filename.replace('.md', '').replace('_', ' ').capitalize()

            # 创建并保存文章
            article = Article.objects.create(title=title, content=content)
            article.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully imported: {filename}'))