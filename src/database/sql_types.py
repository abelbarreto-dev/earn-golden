from sqlalchemy.sql.sqltypes import TypeDecorator

from sqlalchemy import (
    types,
    Dialect,
)

from src.utils.year_month_date import YearMonthDate


class YearMonthDateDB(TypeDecorator):
    impl = types.String(7)

    def get_dbapi_type(self, dbapi):
        return dbapi.YEAR_MONTH_DATE

    @property
    def python_type(self):
        return YearMonthDate

    def process_bind_param(self, value: YearMonthDate, dialect: Dialect) -> str:
        return str(value)

    def process_result_value(self, value: YearMonthDate, dialect: Dialect) -> YearMonthDate:
        return value

    def process_literal_param(self, value: YearMonthDate, dialect: Dialect) -> str:
        return str(value)
