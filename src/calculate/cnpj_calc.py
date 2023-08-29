from src.exceptions.exceptions import CNPJException

from typing import (
    List,
    Generator,
)


class CNPJCalc:
    @classmethod
    def _get_check_digit(cls, sum_all: int) -> int:
        module_eleven = sum_all % 11

        check_digit = (11 - module_eleven, 0)[module_eleven < 2]

        return check_digit

    @classmethod
    def _get_multiply_calc_list(
            cls,
            new_cnpj: Generator[int, None, None],
            digits: List[int]
    ) -> Generator[int, None, None]:
        for x, y in zip(new_cnpj, digits):
            yield x * y

    def _make_operation_check_digits(
            self,
            new_cnpj: Generator[int, None, None],
            digits: List[int]
    ) -> int:
        list_sum_all = self._get_multiply_calc_list(new_cnpj, digits)

        sum_all = sum(i for i in list_sum_all)

        check_digit = self._get_check_digit(sum_all)

        return check_digit

    def _calculate(self, cnpj: str) -> str:
        check_digits = ""

        new_cnpj = [int(i) for i in cnpj]

        check_digit = self._make_operation_check_digits(
            (i for i in new_cnpj),
            [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        )

        check_digits += str(check_digit)
        new_cnpj.append(check_digit)

        check_digit = self._make_operation_check_digits(
            (i for i in new_cnpj),
            [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2],
        )

        new_cnpj.clear()

        check_digits += str(check_digit)

        return check_digits

    def cnpj_calc_checker(self, cnpj: str) -> None:
        if not cnpj.isnumeric():
            raise CNPJException("cnpj should be numeric only")

        if len(cnpj) not in (14, ):
            raise CNPJException("cnpj length should be equals to 14")

        check_digits = self._calculate(cnpj)

        if check_digits not in cnpj[-2: 14]:
            raise CNPJException("cnpj checker digits are not valid")
