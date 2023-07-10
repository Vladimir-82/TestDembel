from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор",
                               )
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name="Категория",
                                 )
    title = models.CharField(max_length=50, verbose_name="Заголовок",)
    body = models.TextField(blank=True, null=True, verbose_name="Контент",)
    views = models.IntegerField(default=0, verbose_name="Просмотры",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Новости"




class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Категория",)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


