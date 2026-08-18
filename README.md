# MyBlog

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A Django-powered blog with full-text search (Whoosh via django-haystack), Markdown
> rendering and captcha protection. —— 基于 Django 的博客应用,集成全文搜索(Whoosh)、
> Markdown 渲染与验证码,附迁移 `init.sh`。

## 🚀 Quick Start

```bash
pip install "setuptools<81"     # provides pkg_resources needed by django-haystack on newer Python
pip install -r requirements.txt
python manage.py migrate        # 初始化数据库
python manage.py runserver      # http://127.0.0.1:8000
```

> 依赖修复:原 `django-haystack==3.0` 与 Django 4.2 不兼容(无法 `manage.py check`),
> 已升级为 `>=3.1`。

## 🗂 Structure

- `blog/` — 核心应用(models / admin / forms / search_indexes / management)
- `myblog/` — 项目配置(settings / urls / wsgi)
- `db.sqlite3`, `whoosh_index/`, `staticfiles/` — 本地数据与静态构建产物(建议 .gitignore)

## ✅ Quality Bar

- `python manage.py check` 通过(需 `django-haystack>=3.1`)。
- 冒烟测试 `blog/tests.py`(SimpleTestCase, 无需数据库)通过。

## 🔬 Verified Demo Evidence

> 短时冒烟运行 —— 证明可安装且可执行 (not a full functional/database run).

```text
$ python manage.py check
System check identified no issues (0 silenced).
$ python manage.py test blog -v1
Found 2 test(s). .. Ran 2 tests in 0.000s  OK
```

## 📄 License

MIT — see `LICENSE`.