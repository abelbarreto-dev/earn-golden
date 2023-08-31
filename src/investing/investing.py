from decimal import Decimal

from os import getenv

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from requests import (
    get as url_open,
    Response,
)

from src.models.models import Quotation


class Investing:
    FEATURE = "html.parser"

    @classmethod
    def _make_request(cls, url) -> Response:
        data_site = url_open(url)

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

        money_str = span_tag[0].text

        money_str = money_str.replace(",", ".")

        return Decimal(money_str)

    def dollar_in_real(self, deps: bool = load_dotenv()) -> Quotation:
        dollar_url = getenv("DOLLAR_REAL")

        dollar = self._get_quotation(dollar_url)

        dollar_real = Quotation(
            description="Dollar In Brazilian Real",
            original=Decimal("1.00"),
            final_value=dollar,
        )

        return dollar_real
