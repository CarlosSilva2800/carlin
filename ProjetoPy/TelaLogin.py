import tkinter as tk
from tkinter import messagebox


class Janela:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Tela de Login")

        self.fontep = ("arial", "10", "bold")

        # Título da janela
        self.titulo = tk.Label(master, text="Login", font=("times new roman", "15", "bold"))
        self.titulo.pack(pady=10)

        # Campo de Usuário
        self.cont_usuario = tk.Frame(master)
        self.cont_usuario["padx"] = 10
        self.cont_usuario.pack(pady=5)
        self.lbl_usuario = tk.Label(self.cont_usuario, text="Usuário:", font=self.fontep)
        self.lbl_usuario.pack(side=tk.LEFT)
        self.ent_usuario = tk.Entry(self.cont_usuario, width=20)
        self.ent_usuario.pack(side=tk.LEFT)

        # Campo de Senha
        self.cont_senha = tk.Frame(master)
        self.cont_senha["padx"] = 10
        self.cont_senha.pack(pady=5)
        self.lbl_senha = tk.Label(self.cont_senha, text="Senha:", font=self.fontep)
        self.lbl_senha.pack(side=tk.LEFT)
        self.ent_senha = tk.Entry(self.cont_senha, width=20, show="*")
        self.ent_senha.pack(side=tk.LEFT)

        # Botão de Login
        self.cont_botoes = tk.Frame(master)
        self.cont_botoes["padx"] = 10
        self.cont_botoes.pack(pady=15)
        self.b_login = tk.Button(self.cont_botoes, text="Login", font=self.fontep, command=self.login)
        self.b_login["width"] = 10
        self.b_login.pack(side=tk.LEFT)

        # Botão de Fechar
        self.b_fechar = tk.Button(self.cont_botoes, text="Fechar", font=self.fontep, command=master.quit)
        self.b_fechar["width"] = 10
        self.b_fechar.pack(side=tk.LEFT, padx=10)

    def login(self):
        usuario = self.ent_usuario.get()
        senha = self.ent_senha.get()

        # Exemplo de validação simples
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")


root = tk.Tk()
Janela(root)
root.mainloop()
