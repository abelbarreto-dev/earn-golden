from typing import Generator

from src.exceptions.exceptions import CPFException


class CPFCalc:
    @classmethod
    def _get_check_digit(cls, sum_all: int) -> int:
        module_eleven = sum_all % 11

        check_digit = (11 - module_eleven, 0)[module_eleven < 2]

        return check_digit

    @classmethod
    def _get_multiply_calc_list(
            cls,
            new_cpf: Generator[int, None, None],
            digit: int = 10,
    ) -> Generator[int, None, None]:
        for index, multi in zip(new_cpf, range(digit, 1, -1)):
            yield index * multi

    def _make_operation_check_digits(
            self,
            new_cpf: Generator[int, None, None],
            digits: int = 10,
    ) -> int:
        list_sum_all = self._get_multiply_calc_list(new_cpf, digits)

        sum_all = sum(i for i in list_sum_all)

        check_digit = self._get_check_digit(sum_all)

        return check_digit

    def _calculate(self, cpf: str) -> str:
        check_digits = ""

        new_cpf = [int(i) for i in cpf[: -2]]

        check_digit = self._make_operation_check_digits(
            (i for i in new_cpf),
        )

        check_digits += str(check_digit)
        new_cpf.append(check_digit)

        check_digit = self._make_operation_check_digits(
            (i for i in new_cpf),
            digits=11
        )

        new_cpf.clear()

        check_digits += str(check_digit)

        return check_digits

    def cpf_calc_checker(self, cpf: str) -> None:
        if not cpf.isnumeric():
            raise CPFException("cpf value should be numeric only")

        if len(cpf) not in (11, ):
            raise CPFException("cpf length should be equals to 11")

        check_digits = self._calculate(cpf)

        if check_digits not in cpf[-2: 11]:
            raise CPFException("cpf checker digits are not valid")
