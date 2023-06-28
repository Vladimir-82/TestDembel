import pytest


@pytest.mark.django_db
def test_post_info(user, category, post) -> None:
    """create information"""
    response = post[0]
    data = response.data

    assert response.status_code == 201
    assert data["title"] == post[1]["title"]
    assert data["body"] == post[1]["body"]
    assert data["views"] == post[1]["views"]
    assert user.pk == post[1]["author"]
    assert category.pk == post[1]["category"]


@pytest.mark.django_db
def test_get_info(auth_client, post) -> None:
    """get information"""
    response = auth_client.get('/api/v1/posts/')

    assert response.status_code == 200
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_get_detail_false_404(auth_client) -> None:
    """get false detail"""
    response = auth_client.get('/api/v1/posts/0/')

    assert response.status_code == 404



@pytest.mark.django_db
def test_update_info(auth_client, user, category, post) -> None:
    """update information"""
    new_data = {"author": user.pk,
                "title": "Shame",
                "body": "Some content",
                "views": 14,
                "category": category.pk,
                }

    response = auth_client.put('/api/v1/posts/1/', new_data)
    data = response.data

    assert data["body"] == new_data["body"]
    assert data["title"] == new_data["title"]
    assert data["views"] == new_data["views"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_info(auth_client, user, category, post) -> None:
    """delete information"""
    response = auth_client.delete('/api/v1/posts/1/')

    assert response.status_code == 204