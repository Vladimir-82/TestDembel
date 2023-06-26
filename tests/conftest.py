import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from app.models import Category


@pytest.fixture
def user():
    """create user"""
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    return user


@pytest.fixture
def client():
    return APIClient()



@pytest.fixture
def auth_client(user, client):
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    return client


@pytest.fixture
def category():
    category = Category.objects.create(title="test_category")
    return category