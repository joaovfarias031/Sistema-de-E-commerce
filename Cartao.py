from Pagamento import Pagamento
class Cartao(Pagamento):
    def __init__(self, id, valor, data, status, Pedido):
        super().__init__(id, valor, data, status, Pedido)
    def processarPagamento(self):
        pass
    def calcularParcelas(self):
        pass