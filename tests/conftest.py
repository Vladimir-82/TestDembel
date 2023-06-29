import pytest
from mixer.backend.django import mixer

from django.contrib.auth.models import User
from rest_framework.test import APIClient

from app.models import Category, Post


@pytest.fixture
def user():
    """create user"""
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    return user


@pytest.fixture
def client():
    """create client"""
    return APIClient()



@pytest.fixture
def auth_client(user, client):
    """create auth_client"""
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    return client


@pytest.fixture
def category():
    """create category"""
    category = Category.objects.create(title="test_category")
    return category



@pytest.fixture
def post(user, auth_client, category):
    """create post"""
    test_object = mixer.blend(Post)

    return test_object