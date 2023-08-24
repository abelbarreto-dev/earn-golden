from sqlalchemy import (
    Integer,
    BigInteger,
    Column,
    String,
    Date,
    ForeignKey,
    Enum,
    DECIMAL,
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


class BankAccount(Base):
    __tablename__ = "bank_accounts"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    bank_id = Column(BigInteger, ForeignKey("banks.id"), nullable=False)
    variation = Column(Integer, nullable=True)
    number = Column(String(64), nullable=False)
    type_account = Column(Enum("payment", "saving", "checking"), nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)


class Card(Base):
    __tablename__ = "cards"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    bank_account_id = Column(BigInteger, ForeignKey("bank_accounts.id"), nullable=False)
    name = Column(String(128), nullable=False)
    number = Column(String(128), nullable=False)
    due_date = Column(Date, nullable=False)
    sec_code = Column(String(16), nullable=False)
    type_card = Column(Enum('credit', 'debit', 'prepaid'), nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    card_id = Column(BigInteger, ForeignKey("cards.id"), nullable=False)
    total_invoice = Column(DECIMAL(10, 2), nullable=False)
    installments = Column(Integer, nullable=False)
    installments_value = Column(DECIMAL(10, 2), nullable=False)
    close_date = Column(Date, nullable=False)
    payment_date = Column(Date, nullable=False)
