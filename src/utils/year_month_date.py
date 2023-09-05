from pydantic import (
    BaseModel,
    model_validator,
)

from src.utils.regex_serch import get_class_name


def _instance_year_month_date(
        class_built: str,
        class_name: str = "YearMonthDate"
) -> None:
    name_class = get_class_name(class_built)

    if name_class not in (class_name, ):
        raise Exception(f"this object is not an instance of {class_name} class.")


class YearMonthDate(BaseModel):
    year: int
    month: int

    @model_validator(mode="after")
    def _check_date(self):
        min_year, max_year = 1, 9999

        if not 0 < self.month < 13:
            raise ValueError(
                f"month value not in 1...12",
                self.month,
            )

        if not min_year <= self.year <= max_year:
            raise ValueError(
                f"year value not in {min_year}...{max_year}",
                self.year,
            )

    def iso_format(self):
        return "%04d-%02d" % (self.year, self.month)

    __str__ = iso_format

    def __lt__(self, other):
        _instance_year_month_date(
            str(type(other))
        )

        if (
                self.year < other.year or
                (self.year == other.year and self.month < other.month)
        ):
            return True

        return False

    def __gt__(self, other):
        _instance_year_month_date(
            str(type(other))
        )

        if (
                self.year > other.year or
                (self.year == other.year and self.month > other.month)
        ):
            return True

        return False

    def __eq__(self, other):
        _instance_year_month_date(
            str(type(other))
        )

        if (self.year, self.month) == (other.year, other.month):
            return True

        return False

    def __le__(self, other):
        _instance_year_month_date(
            str(type(other))
        )

        if self.year <= other.year:
            return self.month <= other.month

        return False

    def __ge__(self, other):
        _instance_year_month_date(
            str(type(other))
        )

        if self.year >= other.year:
            return self.month >= other.month

        return False
