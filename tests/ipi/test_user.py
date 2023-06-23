import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


client = APIClient()


@pytest.mark.django_db
def test_login_user():
    User.objects.create_user(username='test_user', password='Bb*12345678')
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    response = client.post('/api-auth/login/', payload)

    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_user():
    User.objects.create_user(username='test_user', password='Bb*12345678')
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    response = client.post('/api-auth/logout/', payload)

    assert response.status_code == 200