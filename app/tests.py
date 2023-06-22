from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post, Category


class CreatePostTests(APITestCase):
    """
    Tests for my project
    """
    def test_create_post(self):
        """
        create a new object.
        """
        url = reverse('view_create')
        cat = Category.objects.create(title="test_category")
        user = User.objects.create_user(username='test_user',
                                        password='Bb*12345678'
                                        )
        self.client.login(username='test_user', password='Bb*12345678')

        data = {"author": user.pk,
                "title": "Record",
                "body": "Some sport content",
                "views": 32,
                "category": cat.pk,
                }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Record")
        self.assertEqual(Post.objects.get().body, "Some sport content")
        self.assertEqual(Post.objects.get().views, 32)
