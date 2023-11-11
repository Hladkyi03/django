from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    category = models.CharField("Category", max_length=250, help_text="Maximum 250 characters")
    slug = models.SlugField("Slug", default="")

    class Meta:
        verbose_name = "Category for publication"
        verbose_name_plural = "Categories for publications"

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse("articles-category-list", kwargs={"slug": self.slug})
        except:
            url = "/"

        return url


class Article(models.Model):
    title = models.CharField("Title", max_length=250, help_text="Maximum 250 characters")
    description = models.TextField(blank=True, verbose_name="Description")
    pub_date = models.DateTimeField("Date of publication", default=timezone.now)
    slug = models.SlugField("Slug", unique_for_date="pub_date")
    main_page = models.BooleanField("Main", default=False, help_text="Show on the main page")

    category = models.ForeignKey(
        Category, related_name="articles", blank=True, null=True, verbose_name="Category", on_delete=models.CASCADE
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
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name="Article", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField("Photo", upload_to="photos")
    title = models.CharField("Title", max_length=250, help_text="Maximum 250 characters", blank=True)

    @property
    def filename(self):
        return self.image.name.rsplit("/", 1)[-1]

    class Meta:
        verbose_name = "Article Photo"
        verbose_name_plural = "Article Photos"

    def __str__(self):
        return self.title
