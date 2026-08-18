from Pagamento import Pagamento
class Pix(Pagamento):
    def __init__(self, id, valor, data, status, Pedido):
        super().__init__(id, valor, data, status, Pedido)
    def processarPagamento(self):
        pass
    def gerarQRcode(self):
        pass
    