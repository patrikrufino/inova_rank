from http import HTTPStatus


def test_create_category(client):
    response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'name': 'category',
        'id': 1,
    }


def test_create_category_with_same_name(client):
    response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {
        'detail': 'Category already exists',
    }
