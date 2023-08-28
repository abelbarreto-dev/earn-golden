from sqlalchemy.sql.sqltypes import (
    HasExpressionLookup,
    TypeEngine,
)


from src.utils.year_month_date import YearMonthDate


class _RenderISO8601NoT:
    def _literal_processor_date(self, dialect):
        return self._literal_processor_portion(dialect, 0)

    def _literal_processor_portion(self, dialect, _portion=None):
        assert _portion in (None, 0, -1)
        if _portion is not None:

            def process(value):
                if value is not None:
                    value = f"""'{value.isoformat().split("T")[_portion]}'"""
                return value

        else:

            def process(value):
                if value is not None:
                    value = f"""'{value.isoformat().replace("T", " ")}'"""
                return value

        return process


class YearMonthDateDB(_RenderISO8601NoT, HasExpressionLookup, TypeEngine["YearMonthDate"]):
    """A type for ``Year Month Date`` objects."""

    __visit_name__ = "YearMonthDate"

    def get_dbapi_type(self, dbapi):
        return dbapi.DATETIME

    @property
    def python_type(self):
        return YearMonthDate

    def literal_processor(self, dialect):
        return self._literal_processor_date(dialect)
