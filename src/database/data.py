from sqlalchemy import (
    Integer,
    BigInteger,
    Column,
    String,
    Date,
    ForeignKey,
    Enum,
    DECIMAL,
    Boolean,
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
    type_card = Column(Enum("credit", "debit", "prepaid"), nullable=False)
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


class Pix(Base):
    __tablename__ = "pixes"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    bank_account_id = Column(BigInteger, ForeignKey("bank_accounts.id"), nullable=False)
    pix_key_type = Column(Enum("email", "randomic", "mobile", "cpf", "cnpj"), nullable=False)
    pix_key = Column(String(255), nullable=False, unique=True)


class TransferPix(Base):
    __tablename__ = "transfer_pixes"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=False)
    send_pix_type = Column(Enum("mobile", "email", "cpf", "cnpj", "randomic"), nullable=False)
    receiver_pix_type = Column(Enum("mobile", "email", "cpf", "cnpj", "randomic"), nullable=False)
    is_yours = Column(Boolean, default=False)
    send_pix_key = Column(String(255), nullable=False)
    receiver_pix_key = Column(String(255), nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)


class TransferPixAccount(Base):
    __tablename__ = "transfer_pix_accounts"

    id = Column(BigInteger, primary_key=True, nullable=False)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=False)
    pix_id_sender = Column(BigInteger, ForeignKey("pixes.id"), nullable=False)
    pix_id_receiver = Column(BigInteger, ForeignKey("pixes.id"), nullable=True)


class MoneyBox(Base):
    __tablename__ = "money_boxes"

    id = Column(BigInteger, primary_key=True, nullable=False)
    account_id = Column(BigInteger, ForeignKey("accounts.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    objective = Column(DECIMAL(10, 2), nullable=True)
    balance = Column(DECIMAL(10, 2), nullable=False)


class TransferMoneyBox(Base):
    __tablename__ = "transfer_money_boxes"

    id = Column(BigInteger, primary_key=True, nullable=False)
    money_box_id = Column(BigInteger, ForeignKey("money_boxes.id"), nullable=False)
    money_operation = Column(Enum("deposit", "withdraw"), nullable=False)
    balance = Column(DECIMAL(10, 2), nullable=False)
