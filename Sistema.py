from Pedido import Pedido
from Cliente import Cliente
class Sistema:
    def __init__(self):
        self.Pedido = []
        self.Cliente = []
    def cadastrarPedido(self, numero, data, descricao, quantidade, precoUnitario, tipoPagamento):
        pedido = Pedido(numero, data, descricao, quantidade, precoUnitario, tipoPagamento)
        self.Pedido.append(pedido)
    def consultarPedido(self,numero):
        for pedido in self.__pedidos:
            if pedido.getNumero() == numero:
                return pedido

        return None
    def atualizarPedido(self, numero, novoStatus):
            pedido = self.consultarPedido(numero)

            if pedido:
                pedido.setStatus(novoStatus)

    def deletarPedido(self, numero):
        pedido = self.consultarPedido(numero)

        if pedido:
            self.__pedidos.remove(pedido)
    def cadastrarCliente(self, id, nome, email, cpf, telefone):
        cliente = Cliente(id, nome, email, cpf, telefone)
        self.__clientes.append(cliente)

    def consultarCliente(self):
        for cliente in self.__clientes:
            if cliente.getId() == id:
                return cliente

        return None
    def atualizarCliente(self, id, nome, email, telefone):
        cliente = self.consultarCliente(id)

        if cliente:
            cliente.setNome(nome)
            cliente.setEmail(email)
            cliente.setTelefone(telefone)
    def deletarCliente(self):
        cliente = self.consultarCliente(id)

        if cliente:
            self.__clientes.remove(cliente)
