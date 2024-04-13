# conta_bancaria.py
import os


class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            return True
        else:
            return False

    def criar_conta(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.extrato.append(
            f"Conta criada com saldo inicial de R$ {saldo_inicial:.2f}")

    @staticmethod
    def salvar_conta(conta, filename="contas.txt"):
        try:
            with open(filename, "a") as f:
                f.write(f"{conta.saldo}\n")
        except Exception as e:
            print(f"Erro ao salvar conta: {e}")

    @staticmethod
    def carregar_contas(filename="contas.txt"):
        contas = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    saldo = float(line.strip())
                    conta = ContaBancaria()
                    conta.saldo = saldo
                    contas.append(conta)
        return contas
