from http import HTTPStatus

from sqlalchemy import delete

from inova_rank_api.models import Category


def test_create_category(client) -> None:
    response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'category',
    }


def test_create_category_with_same_name(client, session) -> None:
    session.execute(delete(Category).where(Category.name == 'category'))
    session.commit()
    response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT


def test_read_categories(client, session) -> None:
    response = client.get('/categories/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'categories': []}

    session.execute(delete(Category).where(Category.name == 'category'))
    session.add(Category(name='category'))
    session.commit()
    response = client.get('/categories/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'categories': [{'id': 1, 'name': 'category'}]}
