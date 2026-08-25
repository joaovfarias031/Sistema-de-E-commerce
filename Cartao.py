from Pagamento import Pagamento
class Cartao(Pagamento):
    def __init__(self, id, valor, data, status):
        super().__init__(id, valor, data, status)
    def processarPagamento(self):
        print("Processando pagamento via cartão...")
        self._status = "Aprovado"
        return True
    def calcularParcelas(self, quantidadeParcelas):
        return self._valor / quantidadeParcelas
    