from src.exceptions.exceptions import CNPJException

from typing import (
    List,
    Generator,
)


class CNPJCalc:
    def _make_operation_check_digits(
            self,
            new_cpf: Generator[int, None, None],
            digits: List[int]
    ) -> int:
        pass

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

        if check_digits not in cnpj[-2: 11]:
            raise CNPJException("cnpj checker digits are not valid")
