from sqlalchemy import (
    BigInteger,
    Column,
    String,
    Date,
    ForeignKey,
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


class Bank(Base):
    __tablename__ = "banks"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=False)
    name = Column(String(128), nullable=False)
    code = Column(String(32), nullable=False)
    agency = Column(String(32), nullable=False)
