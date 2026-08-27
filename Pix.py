from Pagamento import Pagamento
from rich.console import Console

console = Console()
class Pix(Pagamento):
    def __init__(self, id, valor):
        super().__init__(id, valor)
    def processarPagamento(self):
        console.print(f"valor:{self._valor}",style="bold blue")
        console.print("Processando pagamento via Pix...", style="bold blue")
        self._status = "Aprovado"
        return True


    
    