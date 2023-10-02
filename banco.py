from typing import List
from time import sleep
from colorama import Fore,Back,Style

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()


def menu() -> None:
    print(Fore.GREEN + '======================================')
    print('============== ATM ===================')
    print('=========== Navi Bank ================')

    print(Fore.BLUE + 'Selecione uma opção no menu: ')
    print(Fore.MAGENTA +  '1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print(Fore.YELLOW + 'Volte sempre !')
        sleep(2)
        exit(0)

    else:
        print(Fore.RED + 'Opção inválida')
        sleep(2)
        menu()

def criar_conta() -> None:
    print(Fore.YELLOW + 'Informe os dados do cliente: ')
    nome: str = input('Nome do cliente')
    email: str = input('E-mail do cliente')
    cpf: str = input('CPF do cliente')
    data_nascimento: str = input('Data de nascimento do cliente')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print(Fore.BLUE + 'Conta criada com sucesso.')
    print('Dados da conta:')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int(input('Informe o numero da sua conta'))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input(('Informe o valor do saque')))
            conta.sacar(valor)
        else:
            print(Fore.LIGHTBLACK_EX + f'Não foi encontrada a conta com nume {numero}')

    else:
        print(Fore.CYAN + 'Ainda não existe contas cadastradas')
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
       numero: int = int(input('Informe o numero da sua conta: '))

       conta: Conta = buscar_conta_por_numero(numero)

       if conta:
           valor: float =float(input('Informe o valor do depósito: '))

           conta.depositar(valor)
       else:
           print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print(Fore.CYAN + 'Ainda não exitem contas cadastradas')
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = (input('Informe o número da sua conta:'))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int =int(input('Informe o numero da conta destino:'))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor:float = float(input('Informe o valor da transferencia: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta destino com numero {numero_d} não foi encontrada')
        else:
            print(f'A sua conta com numero {numero_o} não foi encontrada')
    else:
        print(Fore.CYAN + 'Ainda não exite contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas)> 0:
      print('Lista de contas')

      for conta in contas:
          print(conta)
          print('-------------------------')
          sleep(1)

    else:
        print(Fore.CYAN + 'Não exitem contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None


    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__== '__main__':
    main()
