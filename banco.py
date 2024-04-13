# banco.py
from conta_bancaria import ContaBancaria

# Utiliza a mesma instância da classe ContaBancaria definida em conta_bancaria.py
conta = ContaBancaria()

menu = """
Banco Dio

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
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
