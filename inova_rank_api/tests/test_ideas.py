from http import HTTPStatus

from fastapi.testclient import TestClient
from httpx import Response
from sqlalchemy.orm.session import Session


def test_create_idea(client: TestClient) -> None:
    response: Response = client.post(
        '/ideas/',
        json={
            'author_id': 1,
            'title': 'idea',
            'content': 'content',
            'category_id': 1,
        },
    )
    assert response.status_code == HTTPStatus.CREATED


def test_create_idea_with_same_title(client: TestClient) -> None:
    client.post(
        '/ideas/',
        json={
            'author_id': 1,
            'title': 'idea',
            'content': 'content',
            'category_id': 1,
        },
    )

    response: Response = client.post(
        '/ideas/',
        json={
            'author_id': 1,
            'title': 'idea',
            'content': 'content',
            'category_id': 1,
        },
    )
    assert response.status_code == HTTPStatus.CONFLICT
    assert response.json() == {'detail': 'Idea already exists'}


def test_read_ideas(client: TestClient, session: Session) -> None:
    response: Response = client.get('/ideas/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'ideas': []}
