# interface_grafica.py
import tkinter as tk
from tkinter import messagebox
from conta_bancaria import ContaBancaria


def carregar_conta_inicial():
    global conta
    contas = ContaBancaria.carregar_contas()
    conta = contas[-1] if contas else None


def criar_conta():
    saldo_inicial = float(entry_saldo_inicial.get())
    ContaBancaria().criar_conta(saldo_inicial)
    messagebox.showinfo(
        "Sucesso", f"Conta criada com sucesso com saldo inicial de R$ {saldo_inicial:.2f}")
    # Limpa o campo de entrada após a criação da conta
    entry_saldo_inicial.delete(0, tk.END)
    # Atualiza a variável conta para apontar para a nova conta criada
    carregar_conta_inicial()


def confirmar_deposito():
    valor = float(entry_valor.get())
    confirmacao = messagebox.askyesno(
        "Confirmar Depósito", f"Você tem certeza que deseja depositar R$ {valor:.2f}?")
    if confirmacao:
        conta.depositar(valor)
        messagebox.showinfo(
            "Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        # Limpa o campo de entrada após o depósito
        entry_valor.delete(0, tk.END)


def confirmar_saque():
    valor = float(entry_valor.get())
    confirmacao = messagebox.askyesno(
        "Confirmar Saque", f"Você tem certeza que deseja sacar R$ {valor:.2f}?")
    if confirmacao:
        if conta.sacar(valor):
            messagebox.showinfo(
                "Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror(
                "Erro", "Operação falhou! Você não tem saldo suficiente.")
        entry_valor.delete(0, tk.END)  # Limpa o campo de entrada após o saque


def extrato():
    extrato = "\n".join(conta.extrato) or "Não foram realizadas movimentações."
    messagebox.showinfo(
        "Extrato", f"Extrato:\n{extrato}\nSaldo: R$ {conta.saldo:.2f}")


def sair():
    confirmacao = messagebox.askyesno(
        "Sair", "Você tem certeza que deseja sair?")
    if confirmacao:
        root.destroy()


# Carrega a conta inicial ao iniciar o programa
carregar_conta_inicial()

root = tk.Tk()
root.title("Banco Dio")

label_saldo_inicial = tk.Label(root, text="Saldo Inicial:")
label_saldo_inicial.pack()

entry_saldo_inicial = tk.Entry(root)
entry_saldo_inicial.pack()

criar_conta_button = tk.Button(root, text="Criar Conta", command=criar_conta)
criar_conta_button.pack()

label_valor = tk.Label(root, text="Valor:")
label_valor.pack()

entry_valor = tk.Entry(root)
entry_valor.pack()

depositar_button = tk.Button(
    root, text="Depositar", command=confirmar_deposito)
depositar_button.pack()

sacar_button = tk.Button(root, text="Sacar", command=confirmar_saque)
sacar_button.pack()

extrato_button = tk.Button(root, text="Ver Extrato", command=extrato)
extrato_button.pack()

sair_button = tk.Button(root, text="Sair", command=sair)
sair_button.pack()

root.mainloop()
