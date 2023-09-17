from src.repositories.repository_bank_account import RepositoryBankAccount


class ServiceBankAccount:
    _repo_bank_account: RepositoryBankAccount

    def __init__(self):
        self._repo_bank_account = RepositoryBankAccount()

    @property
    def repo_bank_account(self) -> RepositoryBankAccount:
        return self._repo_bank_account
