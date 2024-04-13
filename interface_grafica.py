# interface_grafica.py
import tkinter as tk
from tkinter import messagebox
from conta_bancaria import ContaBancaria

# Utiliza a mesma instância da classe ContaBancaria definida em conta_bancaria.py
conta = ContaBancaria()


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


root = tk.Tk()
root.title("Banco Dio")

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
