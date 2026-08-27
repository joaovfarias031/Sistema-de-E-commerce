from datetime import datetime
class Pagamento:
    def __init__(self, id, valor):
        self._id = id
        self._valor = float(valor)
        self._data = datetime.now()
        self._status = "Pendente"
    def processarPagamento(self):
        self._status = "Aprovado"
        return True
    

