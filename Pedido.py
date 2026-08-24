from ItemPedido import itemPedido
class Pedido:
    def __init__(self, numero, data, status):
        self.__numero = numero
        self.__data = data
        self.__status = status
        self.__itemPedido = itemPedido()

    def adicionarItem(self):
        
    def removerItem(self):
        pass
    def calcularTotal(self):
        pass
    def finalizarPedido(self):
        pass
    def alterarStatus(self):
        pass
