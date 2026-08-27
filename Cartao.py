from Pagamento import Pagamento
from rich.console import Console

console = Console()
class Cartao(Pagamento):
    def __init__(self, id, valor):
        super().__init__(id, valor)
    def processarPagamento(self):
        console.print(f"valor: {self._valor}", style="bold blue")
        console.print("Processando pagamento via cartão...", style="bold blue")
        self._status = "Aprovado"
        return True
    def calcularParcelas(self, quantidadeParcelas):
        return self._valor / quantidadeParcelas
    