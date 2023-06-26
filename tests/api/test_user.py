import pytest


@pytest.mark.django_db
def test_login_user(user, client) -> None:
    """Login user"""
    payload = {'username': 'test_user', 'password': 'Bb*12345678'}
    response = client.post('/api-auth/login/', payload)

    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_user(user, auth_client) -> None:
    """Logout user"""
    response = auth_client.post('/api-auth/logout/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client) -> None:
    """Fail login user"""
    payload = {'username': 'Bob', 'password': 'Bb*123456789'}
    response = client.post('/api-auth/login/', payload)

    assert response.status_code == 200