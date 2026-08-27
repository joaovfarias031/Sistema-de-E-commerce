from Pedido import Pedido
from Cliente import Cliente
from rich.console import Console

console = Console()
class Sistema:
    def __init__(self):
        self.Pedido = []
        self.Cliente = []
    def cadastrarPedido(self, numero, descricao, quantidade, precoUnitario, tipoPagamento):
        pedido = Pedido(numero, descricao, quantidade, precoUnitario, tipoPagamento)
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        cliente = self.Cliente[indice]
        cliente.realizarPedido(pedido)
        self.Pedido.append(pedido)
        pedido.adicionarItem()
        
    def consultarPedido(self):
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        cliente = self.Cliente[indice]
        cliente.consultarPedidos()

    def atualizarPedido(self, novoStatus):
            indice = int(console.input("[bold blue]Informe o indice[/]"))
            if indice >= 0 and indice < len(self.Pedido):
                pedido = self.Pedido[indice]
                pedido.setStatus(novoStatus)
            else:
                console.print("Índice inválido!", style="bold red")

    def deletarPedido(self):
         indice = int(console.input("[bold blue]Informe o indice[/]"))
         if indice >= 0 and indice < len(self.Pedido):
            pedido = self.Pedido[indice]
            self.Pedido.remove(pedido)
            for cliente in self.Cliente:
                if pedido in cliente.getPedidos():
                    cliente.removerPedido(pedido)
                    break
         else:
            console.print("Índice inválido!", style="bold red")
    def cadastrarCliente(self, id, nome, email, cpf, telefone, rua, numero, bairro, cidade, estado, cep):
        cliente = Cliente(id, nome, email, cpf, telefone)
        self.Cliente.append(cliente)
        cliente.adicionarEndereco(rua, numero, bairro, cidade, estado, cep)

    def consultarCliente(self):
        for cliente in self.Cliente:
            console.print(cliente, style="bold purple")

    def atualizarCliente(self, nome, email, telefone, rua, numero, bairro, cidade, estado, cep):
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        if indice >= 0 and indice < len(self.Pedido):
            cliente = self.Cliente[indice]
            cliente.setNome(nome)
            cliente.setEmail(email)
            cliente.setTelefone(telefone)
            cliente.atualizarEndereco(rua, numero, bairro, cidade, estado, cep)
        else:
          console.print("Índice inválido!", style="bold red")  
    def deletarCliente(self):
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        cliente = self.Cliente[indice]
        self.Cliente.remove(cliente)

    def finalizarPedido(self, id):
        indice = int(console.input("[bold blue]Informe o indice[/]"))
        if indice >= 0 and indice < len(self.Pedido):
            pedido = self.Pedido[indice]
            valor = pedido.calcularTotal()
            pedido.finalizarPedido()
            pedido.realizarPagamento(id, valor)
        else:
            console.print("Índice inválido!", style="bold red")