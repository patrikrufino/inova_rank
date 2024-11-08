from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )

    ideas: Mapped[list['Idea']] = relationship(
        init=False, back_populates='author', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Category:
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    ideas: Mapped[list['Idea']] = relationship(
        init=False, back_populates='category', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Idea:
    __tablename__ = 'ideas'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    num_genius: Mapped[int] = mapped_column(init=False, default=0)
    num_stupid: Mapped[int] = mapped_column(init=False, default=0)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
    author: Mapped['User'] = relationship(init=False, back_populates='ideas')
    category: Mapped['Category'] = relationship(
        init=False, back_populates='ideas'
    )
