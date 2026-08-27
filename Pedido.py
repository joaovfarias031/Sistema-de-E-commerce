from ItemPedido import itemPedido
from Cartao import Cartao
from Pix import Pix
from datetime import datetime
from rich.console import Console

console = Console()
class Pedido:
    def __init__(self, numero, descricao, quantidade, precoUnitario, tipoPagamento):
        self.__numero = int(numero)
        self.__data = datetime.now()
        self.__status = "Pendente"
        self.__itemPedido = itemPedido(descricao, quantidade, precoUnitario)
        self.__itens = []
        self.__tipoPagamento = tipoPagamento

    def adicionarItem(self):
        self.__itens.append(self.__itemPedido)

    def calcularTotal(self):
        total = 0
        for item in self.__itens:
            total += item.calcularSubtotal()
        return total
    def finalizarPedido(self):
        self.__status = "Finalizado"

    def realizarPagamento(self, id, valor):
        if self.__tipoPagamento == "Pix":
            pix = Pix(id, valor)
            pix.processarPagamento()
            self.__status = "Pago"

        elif self.__tipoPagamento == "Cartão":
            cartao = Cartao(id, valor)
            cartao.processarPagamento()    
            quantidadeParcelas = console.input("[bold blue]Informe em quantas vezes você vai dividir:[/]") 
            cartao.calcularParcelas(int(quantidadeParcelas))
            self.__status = "Pago"
    def __str__(self):
        return f"numero: {self.__numero}, data: {self.__data}, status: {self.__status}, descrição: {self.__itemPedido.getDescricao()}, quantidade: {self.__itemPedido.getQuantidade()}, preço Unitario: {self.__itemPedido.getPrecoUnitario()}, tipoPagamento: {self.__tipoPagamento}"
    
    def setStatus(self, status):
        self.__status = status

    

