# banco.py
from conta_bancaria import ContaBancaria

contas = ContaBancaria.carregar_contas()

menu = """
Banco Dio

[c] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "c":
        saldo_inicial = float(input("Informe o saldo inicial da conta: "))
        conta = ContaBancaria()
        conta.criar_conta(saldo_inicial)
        contas.append(conta)
        ContaBancaria.salvar_conta(conta)
        print("Conta criada com sucesso!")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        conta.depositar(valor)
        print("Depósito realizado com sucesso!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if conta.sacar(valor):
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("\n".join(conta.extrato) or "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {conta.saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Sessão Finalizada!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    input("Pressione Enter para continuar...")
