class itemPedido:
    def __init__(self, descricao, quantidade, precoUnitario):
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__precoUnitario = precoUnitario
    def calcularSubtotal(self):
        return self.__quantidade * self.__precoUnitario
    def alterarQuantidade(self, novaQuantidade):
        self.__quantidade = novaQuantidade