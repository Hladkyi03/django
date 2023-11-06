from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    category = models.CharField("Категорія", max_length=250, help_text="Максимум 250 символів")
    slug = models.SlugField("Slug", default="")

    class Meta:
        verbose_name = "Категорія для публікації"
        verbose_name_plural = "Категорії для публікації"

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse("articles-category-list", kwargs={"slug": self.slug})
        except:
            url = "/"

        return url


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=250, help_text="Максимум 250 символів")
    description = models.TextField(blank=True, verbose_name="Опис")
    pub_date = models.DateTimeField("Дата публікації", default=timezone.now)
    slug = models.SlugField("Slug", unique_for_date="pub_date")
    main_page = models.BooleanField("Головна", default=False, help_text="Показувати на головній сторінці")

    category = models.ForeignKey(
        Category, related_name="articles", blank=True, null=True, verbose_name="Категорія", on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        try:
            url = reverse(
                "news-detail",
                kwargs={
                    "year": self.pub_date.strftime("%Y"),
                    "month": self.pub_date.strftime("%m"),
                    "day": self.pub_date.strftime("%d"),
                    "slug": self.slug,
                },
            )
        except:
            url = "/"

        return url

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name="Статті", related_name="зображення", on_delete=models.CASCADE)
    image = models.ImageField("Зображення", upload_to="photos")
    title = models.CharField("Заголовок", max_length=250, help_text="Максимум 250 символів", blank=True)

    @property
    def filename(self):
        return self.image.name.rsplit("/", 1)[-1]

    class Meta:
        verbose_name = "Зображення для статті"
        verbose_name_plural = "Зображення для статті"

    def __str__(self):
        return self.title
