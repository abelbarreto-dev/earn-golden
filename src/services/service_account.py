from src.repositories.repository_account import RepositoryAccount


class ServiceAccount:
    _repo_account: RepositoryAccount

    def __init__(self):
        self._repo_account = RepositoryAccount()

    @property
    def repo_account(self) -> RepositoryAccount:
        return self._repo_account
