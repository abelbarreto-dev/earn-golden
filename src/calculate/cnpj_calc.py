from src.exceptions.exceptions import CNPJException


class CNPJCalc:
    def _calculate(self) -> str:
        return ""

    def cnpj_calc_checker(self, cnpj: str) -> None:
        if not cnpj.isnumeric():
            raise CNPJException("cnpj should be numeric only")

        if len(cnpj) not in (14, ):
            raise CNPJException("cnpj length should be equals to 14")

        check_digits = self._calculate(cnpj)

        if check_digits not in cnpj[-2: 11]:
            raise CNPJException("cnpj checker digits are not valid")
