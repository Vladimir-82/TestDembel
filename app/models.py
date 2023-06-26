from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               )
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.PROTECT,
                                 )
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title




class Category(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title


