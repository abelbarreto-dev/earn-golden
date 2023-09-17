from src.repositories.repository_invoice import RepositoryInvoice


class ServiceInvoice:
    _repo_invoice: RepositoryInvoice

    def __init__(self):
        self._repo_invoice = RepositoryInvoice()

    @property
    def repo_invoice(self) -> RepositoryInvoice:
        return self._repo_invoice
