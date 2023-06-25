import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from app.models import Category

client = APIClient()


@pytest.mark.django_db
def test_post_info() -> None:
    """create information"""
    cat = Category.objects.create(title="test_category")
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    new_data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    response = client.post('/api/v1/posts/', new_data)
    data = response.data

    assert response.status_code == 201
    assert data["title"] == new_data["title"]
    assert data["body"] == new_data["body"]
    assert data["views"] == new_data["views"]
    assert user.pk == new_data["author"]
    assert cat.pk == new_data["category"]


@pytest.mark.django_db
def test_get_info() -> None:
    """get information"""
    cat = Category.objects.create(title="test_category")
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    new_data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    client.post('/api/v1/posts/', new_data)
    response = client.get('/api/v1/posts/')

    assert response.status_code == 200
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_get_detail_false_404() -> None:
    """get false detail"""
    response = client.get('/api/v1/posts/0/')

    assert response.status_code == 404



@pytest.mark.django_db
def test_update_info() -> None:
    """update information"""
    cat = Category.objects.create(title="test_category")
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    old_data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    client.post('/api/v1/posts/', old_data)

    new_data = {"author": user.pk,
                "title": "Shame",
                "body": "Pidori",
                "views": 14,
                "category": cat.pk,
                }

    response = client.put('/api/v1/posts/1/', new_data)
    data = response.data
    assert data["body"] == new_data["body"]
    assert data["title"] == new_data["title"]
    assert data["views"] == new_data["views"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_info() -> None:
    """delete information"""
    cat = Category.objects.create(title="test_category")
    user = User.objects.create_user(username='test_user',
                                    password='Bb*12345678'
                                    )
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    client.post('/api-auth/login/', payload)

    data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    client.post('/api/v1/posts/', data)

    response = client.delete('/api/v1/posts/1/')
    assert response.status_code == 204