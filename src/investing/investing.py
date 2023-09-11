from decimal import Decimal

from os import getenv

from re import match

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from requests import (
    get as url_open,
    Response,
)

from src.exceptions.exceptions import QuotationException

from src.models.models import Quotation

from src.utils.enums import CheckRegex


class Investing:
    load_dotenv()
    FEATURE = "html.parser"

    @classmethod
    def _make_request(cls, url) -> Response:
        data_site = url_open(url)

        if data_site.status_code not in (200, ):
            raise QuotationException("failed the make investing site request")

        return data_site

    def _get_quotation(self, url: str):
        investing = self._make_request(url).content

        extract = BeautifulSoup(investing, self.FEATURE)

        span_tag = extract.find_all(
            "span",
            {
                "class": "text-2xl"
            },
            True
        )

        if not span_tag:
            raise QuotationException("failed to access the specified tag and it parameter")

        money_str = span_tag[0].text

        if not match(CheckRegex.MONEY_COMMON.value, money_str):
            raise QuotationException("money format invalid here")

        money_str = money_str.replace(",", ".")

        return Decimal(money_str)

    def dollar_in_real(self) -> Quotation:

        dollar_url = getenv("DOLLAR_REAL")

        dollar = self._get_quotation(dollar_url)

        dollar_real = Quotation(
            description="Dollar In Brazilian Real",
            original=Decimal("1.00"),
            final_value=dollar,
        )

        return dollar_real

    def pound_in_real(self) -> Quotation:
        pound_url = getenv("POUND_REAL")

        pound = self._get_quotation(pound_url)

        pound_real = Quotation(
            description="British Pound In Brazilian Real",
            original=Decimal("1.00"),
            final_value=pound,
        )

        return pound_real

    def euro_in_real(self) -> Quotation:
        euro_url = getenv("EURO_REAL")

        euro = self._get_quotation(euro_url)

        euro_real = Quotation(
            description="Euro In Brazilian Real",
            original=Decimal("1.00"),
            final_value=euro,
        )

        return euro_real
