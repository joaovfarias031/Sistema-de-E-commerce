from datetime import datetime
class Pagamento:
    def __init__(self, id, valor, data=datetime.now(), status="Pendente"):
        self._id = id
        self._valor = valor
        self._data = data
        self._status = status
    def processarPagamento(self):
        self._status = "Aprovado"
        return True
    def cancelarPagamento(self):
        if self._status == "Aprovado":
            self._status = "Cancelado"
            return True
        return False 
    def consultarStatus(self):
        return self._status

    def getId(self):
        return self.__id

    def getValor(self):
        return self.__valor

    def getData(self):
        return self.__data

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status
