from sqlalchemy import (
    BigInteger,
    Column,
    String,
    Date,
)

from src.database.connection import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cpf = Column(String(12), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    mobile = Column(String(20), nullable=False)
