from Pagamento import Pagamento
class Pix(Pagamento):
    def __init__(self, id, valor, data, status):
        super().__init__(id, valor, data, status)
    def processarPagamento(self):
        print("Processando pagamento via Pix...")
        self._status = "Aprovado"
        return True


    
    