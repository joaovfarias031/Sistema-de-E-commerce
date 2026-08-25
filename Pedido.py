from ItemPedido import itemPedido
from Cartao import Cartao
from Pix import Pix
class Pedido:
    def __init__(self, numero, data, descricao, quantidade, precoUnitario, tipoPagamento):
        self.__numero = numero
        self.__data = data
        self.__status = "Pendente"
        self.__itemPedido = itemPedido(descricao, quantidade, precoUnitario)
        self.__itens = []
        self.__tipoPagamento = tipoPagamento

    def adicionarItem(self):
        self.__itens.append(self.__itemPedido)
    def removerItem(self, item):
        if item in self.__itens:
            self.__itens.remove(item)
    def calcularTotal(self):
        total = 0
        for item in self.__itens:
            total += item.calcularSubtotal()
    def finalizarPedido(self):
        self.__status = "Finalizado"
    def alterarStatus(self, novoStatus):
        self.__status = novoStatus

    def realizarPagamento(self, id, valor, data, status):
        if self.__tipoPagamento == "Pix":
            pix = Pix(id, valor, data, status)
            pix.processarPagamento()
            self.__status = "Pago"

        elif self.__tipoPagamento == "Cartão":
            cartao = Cartao(id, valor, data, status)
            cartao.processarPagamento()     
            self.__status = "Pago"

    def getNumero(self):
        return self.__numero

    def getData(self):
        return self.__data

    def getStatus(self):
        return self.__status

    def getItens(self):
        return self.__itens

    def getPagamento(self):
        return self.__pagamento

    def setStatus(self, status):
        self.__status = status

    

