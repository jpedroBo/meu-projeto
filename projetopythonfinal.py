import tkinter as tk
from tkinter import messagebox
import re

def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao_email, email)

def cadastrar_usuario():
    nome = entrada_nome.get()
    email = entrada_email.get()

    if nome and validar_email(email):
        messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
        limpar_campos()
    else:
        if not nome:
            messagebox.showwarning("Erro", "Por favor, preencha o nome.")
        elif not validar_email(email):
            messagebox.showwarning("Erro", "Por favor, insira um e-mail válido.")

def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_nome.focus_set()  # Voltar o foco para o nome

def focar_proximo_campo(event, campo_atual, proximo_campo=None):
    if campo_atual.get():
        if proximo_campo:
            proximo_campo.focus_set()  # Move o foco para o próximo campo
        else:
            cadastrar_usuario()  # Cadastra o usuário se for o último campo
    else:
        messagebox.showwarning("Erro", "Por favor, preencha este campo.")

janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("400x500")
janela.configure(bg="#2c3e50")  # Fundo escuro

cor_fundo = "#2c3e50"
cor_detalhe = "#ecf0f1"  # Cor clara para contraste
cor_botao = "#1abc9c"
cor_texto = "#ffffff"
fonte_titulo = ("Helvetica", 18, "bold")
fonte_labels = ("Helvetica", 12)
fonte_entrada = ("Helvetica", 12)

label_titulo = tk.Label(janela, text="Cadastro de Usuário", font=fonte_titulo, bg=cor_fundo, fg=cor_detalhe)
label_titulo.pack(pady=20)

frame_formulario = tk.Frame(janela, bg=cor_fundo)
frame_formulario.pack(pady=20)

label_nome = tk.Label(frame_formulario, text="Nome:", font=fonte_labels, bg=cor_fundo, fg=cor_detalhe)
label_nome.grid(row=0, column=0, sticky="w", pady=10)
entrada_nome = tk.Entry(frame_formulario, font=fonte_entrada, width=30, bd=2, relief="flat")
entrada_nome.grid(row=0, column=1, pady=10, padx=10)

label_email = tk.Label(frame_formulario, text="Email:", font=fonte_labels, bg=cor_fundo, fg=cor_detalhe)
label_email.grid(row=1, column=0, sticky="w", pady=10)
entrada_email = tk.Entry(frame_formulario, font=fonte_entrada, width=30, bd=2, relief="flat")
entrada_email.grid(row=1, column=1, pady=10, padx=10)

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_usuario, font=("Helvetica", 14, "bold"), bg=cor_botao, fg=cor_texto, bd=0, width=15, height=2, relief="flat")
botao_cadastrar.pack(pady=30)

entrada_nome.bind("<Return>", lambda event: focar_proximo_campo(event, entrada_nome, entrada_email))
entrada_email.bind("<Return>", lambda event: focar_proximo_campo(event, entrada_email))

janela.mainloop()
