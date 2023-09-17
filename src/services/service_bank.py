from src.repositories.repository_bank import RepositoryBank


class ServiceBank:
    _repo_bank: RepositoryBank

    def __init__(self):
        self._repo_bank = RepositoryBank()

    @property
    def repo_bank(self) -> RepositoryBank:
        return self._repo_bank
