from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)
    description = models.TextField()
    link = models.URLField()
    image = models.FileField(upload_to='images/news_images')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    image = models.FileField(upload_to='images/news_images')
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, related_name='images')

    def __str__(self):
        return self.image.url


LAW_TYPES = (
    (1, 'Действуещее законодательство'),
    (2, 'Проекты нормативных-правовых актов'),
    (3, 'Международные документы'),
)


class Law(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=LAW_TYPES, default=1)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


PUBLIC_TYPES = (
    (1, 'ICNL'),
    (2, 'Other'),
)


class Public(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=PUBLIC_TYPES, default=1)
    created_date = models.DateField(auto_now_add=True)


class NewsFavourite(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)