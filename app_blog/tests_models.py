from django.test import TestCase
from .models import Category, Article


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test
        Category.objects.create(category='Innovations', slug='innovations')

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/articles/category/innovations')

    def test_category_str_representation(self):
        category = Category.objects.get(id=1)
        self.assertEquals(str(category), 'Innovations')


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='innovations')
        Article.objects.create(
            title='Sample Article',
            description='This is a sample article',
            slug='sample-article',
            category=Category.objects.get(id=1),
        )

    def test_get_absolute_url(self):
        article = Article.objects.get(id=1)
        expected_url = '/articles/2023/11/06/sample-article'
        self.assertEquals(article.get_absolute_url(), expected_url)

    def test_article_str_representation(self):
        article = Article.objects.get(id=1)
        self.assertEquals(str(article), 'Sample Article')

    def test_article_has_category(self):
        article = Article.objects.get(id=1)
        self.assertIsNotNone(article.category)
