import pytest


@pytest.mark.django_db
def test_get_info(auth_client, post) -> None:
    """get information"""
    response = auth_client.get('/api/v1/posts/')
    data = response.data

    assert response.status_code == 200
    assert data["count"] == 1
    assert data["results"][0]["user_name"] == post.author.username
    assert data["results"][0]["title"] == post.title
    assert data["results"][0]["body"] == post.body
    assert data["results"][0]["views"] == post.views
    assert data["results"][0]["category"] == post.category.pk



@pytest.mark.django_db
def test_get_detail_false_404(auth_client) -> None:
    """get false detail"""
    response = auth_client.get('/api/v1/posts/0/')

    assert response.status_code == 404



@pytest.mark.django_db
def test_update_info(auth_client, post) -> None:
    """update information"""
    new_data = {"title": "Shame",
                "body": "Some_content",
                "views": 14,
                }

    response = auth_client.put(f'/api/v1/posts/{post.pk}/', new_data)
    data = response.data

    assert data["body"] == new_data["body"]
    assert data["title"] == new_data["title"]
    assert data["views"] == new_data["views"]
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_info(auth_client, post) -> None:
    """delete information"""
    response = auth_client.delete(f'/api/v1/posts/{post.pk}/')

    assert response.status_code == 204