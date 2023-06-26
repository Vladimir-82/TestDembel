import pytest


@pytest.mark.django_db
def test_post_info(auth_client, user, cat) -> None:
    """create information"""
    created = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    response = auth_client.post('/api/v1/posts/', created)

    data = response.data

    assert response.status_code == 201
    assert data["title"] == created["title"]
    assert data["body"] == created["body"]
    assert data["views"] == created["views"]
    assert user.pk == created["author"]
    assert cat.pk == created["category"]


@pytest.mark.django_db
def test_get_info(auth_client, user, cat) -> None:
    """get information"""
    new_data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    auth_client.post('/api/v1/posts/', new_data)
    response = auth_client.get('/api/v1/posts/')

    assert response.status_code == 200
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_get_detail_false_404(auth_client) -> None:
    """get false detail"""
    response = auth_client.get('/api/v1/posts/0/')

    assert response.status_code == 404



@pytest.mark.django_db
def test_update_info(auth_client, user, cat) -> None:
    """update information"""
    old_data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    auth_client.post('/api/v1/posts/', old_data)

    new_data = {"author": user.pk,
                "title": "Shame",
                "body": "Pidori",
                "views": 14,
                "category": cat.pk,
                }

    response = auth_client.put('/api/v1/posts/1/', new_data)
    data = response.data
    assert data["body"] == new_data["body"]
    assert data["title"] == new_data["title"]
    assert data["views"] == new_data["views"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_info(auth_client, user, cat) -> None:
    """delete information"""

    data = {"author": user.pk,
            "title": "Record",
            "body": "Some sport content",
            "views": 32,
            "category": cat.pk,
            }

    auth_client.post('/api/v1/posts/', data)

    response = auth_client.delete('/api/v1/posts/1/')
    assert response.status_code == 204