from sqlalchemy import (
    create_engine,
    Engine,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session,
)

from src.utils.db_urls import get_mysql_url


def get_engine() -> Engine:
    database_url = get_mysql_url()

    engine = create_engine(database_url, echo=True)

    return engine


def get_session(engine: Engine = get_engine()) -> Session:
    new_session = sessionmaker(bind=engine)
    session = new_session()

    return session


Base = declarative_base()
