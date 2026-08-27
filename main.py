from Sistema import Sistema
from rich.console import Console
import os

sistema = Sistema()
console = Console()

while True:
    os.system("cls")
    console.print("\n===== SISTEMA DE E-COMMERCE =====", style="bold red")
    console.print("1 - Cadastrar cliente", style="bold purple")
    console.print("2 - Consultar cliente", style="bold purple")
    console.print("3 - Atualizar cliente", style="bold purple")
    console.print("4 - Deletar cliente", style="bold purple")
    console.print("5 - Cadastrar pedido", style="bold purple")
    console.print("6 - Consultar pedido", style="bold purple")
    console.print("7 - Atualizar pedido", style="bold purple")
    console.print("8 - Deletar pedido", style="bold purple")
    console.print("9 - Finalizar pedido", style="bold purple")
    console.print("10 - Sair", style="bold purple")

    opcao = console.input("[bold red]Escolha uma opção: [/]")

    if opcao == "1":
        id = console.input("[bold blue]Informe um id:[/]")
        nome = console.input("[bold blue]Informe seu nome:[/]")
        email = console.input("[bold blue]Informe seu email:[/]")
        cpf = console.input("[bold blue]Informe o seu cpf:[/]")
        telefone = console.input("[bold blue]Informe o seu telefone:[/]")
        rua = console.input("[bold blue]Informe a sua rua:[/] ")
        numeroEnd = console.input("[bold blue]Informe o número do seu endereço:[/]")
        bairro = console.input("[bold blue]Informe o seu bairro:[/]")
        cidade = console.input("[bold blue]Informe a sua cidade:[/]")
        estado = console.input("[bold blue]Informe o seu estado:[/]")
        cep = console.input("[bold blue]Informe o cep do seu endereço:[/]")
        sistema.cadastrarCliente(id, nome, email, cpf, telefone, rua, numeroEnd, bairro, cidade, estado, cep)


    elif opcao == "2":
        sistema.consultarCliente()
        console.input("[bold blue]Precione ENTER para continuar:[/]")

    elif opcao == "3":
        novoNome = console.input("[bold blue]Informe o seu novo nome:[/]")
        novoEmail = console.input("[bold blue]Informe o seu novo email:[/]")
        novoTelefone = console.input("[bold blue]Informe o seu novo telefone:[/]") 
        novaRua = console.input("[bold blue]Informe a sua nova rua:[/] ")
        novoNumeroEnd = console.input("[bold blue]Informe o  novo número do seu endereço:[/]")
        novoBairro = console.input("[bold blue]Informe o seu novo bairro:[/]")
        novaCidade = console.input("[bold blue]Informe a sua nova cidade:[/]")
        novoEstado = console.input("[bold blue]Informe o seu novo estado:[/]")
        novoCep = console.input("[bold blue]Informe o novo cep do seu endereço:[/]")
        sistema.atualizarCliente(novoNome, novoEmail, novoTelefone, novaRua, novoNumeroEnd, novoBairro, novaCidade, novoEstado, novoCep)

    elif opcao == "4":
        sistema.deletarCliente()

    elif opcao == "5":
        numero = console.input("[bold blue]Informe o número do pedido:[/]")
        descricao = console.input("[bold blue]Informe a descrição do item:[/]")
        quantidade = console.input("[bold blue]Informe a quantidade do item:[/]")
        precoUnitario = console.input("[bold blue]Informe o preço do item:[/]")
        tipoPagamento = console.input("[bold blue]Informe o tipo de pagamento[/]")
        sistema.cadastrarPedido(numero, descricao, quantidade, precoUnitario, tipoPagamento)


    elif opcao == "6":
        sistema.consultarPedido()
        console.input("[bold blue]Precione ENTER para continuar:[/]")

    elif opcao == "7":
        novoStatus = console.input("[bold blue]Informe o novo status do pedido:[/]")
        sistema.atualizarPedido(novoStatus)

    elif opcao == "8":
        sistema.deletarPedido()

    elif opcao == "9":
        id = console.input("[bold blue]Informe o id:[/]")
        sistema.finalizarPedido(id)
        console.input("[bold blue]Precione ENTER para continuar:[/]")


    elif opcao == "10":
        console.print("Encerrando o sistema...", style="bold purple")
        break

    else:
        print("Opção inválida.")