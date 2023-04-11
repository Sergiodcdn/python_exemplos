import tkinter as tk

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def cadastrar_pessoa():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    p1 = Pessoa(nome, idade)
    label_info.config(text=f"O nome é {p1.nome} e a idade é {p1.idade}.")

janela = tk.Tk()
janela.title("Cadastro de Pessoa")

label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_pessoa)
botao_cadastrar.pack()

label_info = tk.Label(janela)
label_info.pack()

janela.mainloop()
