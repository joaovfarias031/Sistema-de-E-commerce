from Endereco import Endereco
from Pedido import Pedido
class Cliente:
    def __init__(self, id, nome, email, cpf, telefone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__telefone = telefone
        self.__Endereco = []
        self.__Pedidos = []

    def realizarPedido(self):
        pedido = Pedido(numero, data, status)
        self.__Pedidos.append(pedido)
    def consultarPedidos(self):
        return self.Pedidos
    def adicionarEndereco(self):
        endereco = Endereco(rua, numero, bairro, cidade, estado, cep)
        self.__Endereco.append(endereco)
    def excluirEndereco(self, endereco):
        if endereco in self.__Endereco:
            self.__Endereco.remove(endereco)