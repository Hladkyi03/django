from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)


class ArticleTests(TestCase):
    def test_article_list_view_status_code(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_list_url_resolves_view(self):
        view = resolve('/articles')
        self.assertEquals(view.func.view_class, ArticleList)

    def test_article_category_list_view_status_code(self):
        # Assuming "name" is a valid category slug for testing
        url = reverse('articles-category-list', args=("name",))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_category_list_url_resolves_view(self):
        view = resolve('/articles/category/name')
        self.assertEquals(view.func.view_class, ArticleCategoryList)

    def test_article_detail_url_resolves_view(self):
        view = resolve('/articles/2023/11/06/example-slug')
        self.assertEquals(view.func.view_class, ArticleDetail)
