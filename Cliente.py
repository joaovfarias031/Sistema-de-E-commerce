from Endereco import Endereco
class Cliente:
    def __init__(self, id, nome, email, cpf, telefone, Endereco):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__telefone = telefone
        self.__Endereco = Endereco

    def realizarPedido(self):
        pass
    def consultarPedidos(self):
        pass
    def adicionarEndereco(self):
        pass
    def excluirEndereco(self):
        pass