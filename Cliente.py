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

    def realizarPedido(self, numero, data, status):
        pedido = Pedido(numero, data, status)
        self.__Pedidos.append(pedido)
    def consultarPedidos(self):
        return self.Pedidos
    def adicionarEndereco(self,rua, numero, bairro, cidade, estado, cep):
        endereco = Endereco(rua, numero, bairro, cidade, estado, cep)
        self.__Endereco.append(endereco)
    def excluirEndereco(self, endereco):
        if endereco in self.__Endereco:
            self.__Endereco.remove(endereco)

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getEmail(self):
        return self.__email

    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setEmail(self, email):
        self.__email = email

    def setTelefone(self, telefone):
        self.__telefone = telefone