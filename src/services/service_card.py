from src.repositories.repository_card import RepositoryCard


class ServiceCard:
    _repo_card: RepositoryCard

    def __init__(self):
        self._repo_card = RepositoryCard()

    @property
    def repo_card(self) -> RepositoryCard:
        return self._repo_card
