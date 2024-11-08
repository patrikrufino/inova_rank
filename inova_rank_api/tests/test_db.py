from dataclasses import asdict

from sqlalchemy import select

from inova_rank_api.models import Category, Idea, User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
        'ideas': [],
    }


def test_create_category(session, mock_db_time):
    with mock_db_time(model=Category):
        new_category = Category(name='test')
        session.add(new_category)
        session.commit()

    category = session.scalar(select(Category).where(Category.name == 'test'))

    assert asdict(category) == {
        'id': 1,
        'name': 'test',
        'ideas': [],
    }


def test_create_idea(user, category, session, mock_db_time):
    with mock_db_time(model=Idea):
        new_idea = Idea(
            title='test',
            content='test',
            category_id=category.id,
            author_id=user.id,
        )
        print(new_idea)
        session.add(new_idea)
        session.commit()

    idea = session.scalar(select(Idea).where(Idea.title == 'test'))
    user = session.scalar(select(User).where(User.id == user.id))

    assert idea in user.ideas
