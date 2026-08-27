class itemPedido:
    def __init__(self, descricao, quantidade, precoUnitario):
        self.__descricao = descricao
        self.__quantidade = int(quantidade)
        self.__precoUnitario = float(precoUnitario)
    def calcularSubtotal(self):
        return self.__quantidade * self.__precoUnitario
    def getDescricao(self):
        return self.__descricao

    def getQuantidade(self):
        return self.__quantidade

    def getPrecoUnitario(self):
        return self.__precoUnitario