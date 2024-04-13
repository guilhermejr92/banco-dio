# conta_bancaria.py
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
