from src.repositories.repository_deposit import RepositoryDeposit


class ServiceDeposit:
    _repo_deposit: RepositoryDeposit

    def __init__(self):
        self._repo_deposit = RepositoryDeposit()

    @property
    def repo_deposit(self) -> RepositoryDeposit:
        return self._repo_deposit
