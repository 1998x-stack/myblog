"""Minimal smoke tests for the blog app (no DB required)."""
from django.test import SimpleTestCase


class BlogSmokeTest(SimpleTestCase):
    def test_blog_app_modules_import(self):
        import blog.admin  # noqa: F401
        import blog.forms  # noqa: F401
        import blog.models  # noqa: F401

    def test_blog_app_config_ready(self):
        from django.apps import apps

        self.assertTrue(apps.is_installed("blog"))