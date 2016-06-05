from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "Posts"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
