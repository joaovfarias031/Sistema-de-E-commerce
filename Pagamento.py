from Pedido import pedido
class Pagamento:
    def __init__(self, id, valor, data, status, Pedido ):
        self.__id = id
        self.__valor = valor
        self.__data = data
        self.__status = status
        self.__Pedido = Pedido
    def processarPagamento(self):
        pass
    def cancelarPagamento(self):
        pass
    def consultarStatus(self):
        pass
