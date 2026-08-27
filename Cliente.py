from Endereco import Endereco
from Pedido import Pedido
from rich.console import Console
console = Console()
class Cliente:
    def __init__(self, id, nome, email, cpf, telefone):
        self.__id = int(id)
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__telefone = telefone
        self.__Endereco = []
        self.__Pedidos = []

    def realizarPedido(self, pedido):
        self.__Pedidos.append(pedido)
    def consultarPedidos(self):
        for pedido in self.__Pedidos:
                    console.print(pedido, style="bold purple")
    def adicionarEndereco(self,rua, numero, bairro, cidade, estado, cep):
        endereco = Endereco(rua, numero, bairro, cidade, estado, cep)
        self.__Endereco.append(endereco)

    def atualizarEndereço(self,rua, numero, bairro, cidade, estado, cep):
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        if indice >= 0 and indice < len(self.Pedido):
           endereco = self.__Endereco[indice]
           endereco.atualizarEndereco(rua, numero, bairro, cidade, estado, cep)
        else:
            console.print("Índice inválido!", style="bold red")
    
    def __str__(self):
        return f"id: {self.__id}, nome: {self.__nome}, email: {self.__email}, cpf: {self.__cpf}, telefone: {self.__telefone}"
    def removerPedido(self, pedido):
        if pedido in self.__Pedidos:
            self.__Pedidos.remove(pedido)
    def getPedidos(self):
        return self.__Pedidos

    def setNome(self, nome):
        self.__nome = nome

    def setEmail(self, email):
        self.__email = email

    def setTelefone(self, telefone):
        self.__telefone = telefone