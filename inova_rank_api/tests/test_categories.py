from http import HTTPStatus

from fastapi.testclient import TestClient
from httpx import Response
from sqlalchemy.orm.session import Session


def test_create_category(client: TestClient) -> None:
    response: Response = client.post(
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


def test_create_category_with_same_name(
    client: TestClient, session: Session
) -> None:
    response: Response = client.post(
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


def test_read_categories(client: TestClient, session: Session) -> None:
    response: Response = client.get('/categories/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'categories': []}


def test_read_category(client: TestClient, session: Session) -> None:
    response: Response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    response = client.get('/categories/category')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 'category',
    }


def test_read_category_not_found(client: TestClient, session: Session) -> None:
    response = client.get('/categories/category')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_category(client: TestClient, session: Session) -> None:
    response: Response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    response = client.delete('/categories/category')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Category deleted successfully'}
    response = client.get('/categories/category')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_category_with_not_found(
    client: TestClient, session: Session
) -> None:
    response = client.delete('/categories/category')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_get_category_id(client: TestClient, session: Session) -> None:
    response: Response = client.post(
        '/categories/',
        json={
            'name': 'category',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    response = client.get('/categories/id/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 'category',
    }
