from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Category
from django.contrib.auth.models import User



class CreatePostTests(APITestCase):
    def test_create_post(self):
        """
        create a new object.
        """
        url = reverse('view_create')

        cat = Category.objects.create(title="testcategory")
        user = User.objects.create_user(username="Testuser")

        data = {"author": user,
                "title": "Recordd",
                "body": "Some sport content",
                "views": "32",
                "category": cat,
                }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Recordd")
