from decimal import Decimal

from os import getenv

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from requests import (
    get as url_open,
    Response,
)


class Investing:
    FEATURE = "html.parser"

    def _make_request(self, url) -> Response:
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

    def dollar_in_real(self, deps: bool = load_dotenv()):
        dollar_url = getenv("DOLLAR_REAL")

        dollar = self._get_quotation(dollar_url)
