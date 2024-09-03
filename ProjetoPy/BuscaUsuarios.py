import tkinter as tk
from tkinter import *
from usuarios import \
    Usuarios  # Certifique-se de que o módulo usuario.py e a classe Usuarios estão corretamente implementados.


class Busca:
    def __init__(self, master=None):
        self.fontep = ("arial", "10", "bold")

        # Título
        self.titulo1 = Label(master, text="Informe os dados:", font=("times new roman", "13", "bold"))
        self.titulo1.pack()

        # Container 2: ID do Usuário e Botão de Busca
        self.cont2 = Frame(master, padx=30)
        self.cont2.pack()
        self.idusu = Label(self.cont2, text="IDusuario:", font=self.fontep)
        self.idinfo = Entry(self.cont2, width=10)
        self.b1 = Button(self.cont2, text="Buscar", font=self.fontep, width=6, command=self.buscar_usuario)
        self.idusu.pack(side=LEFT)
        self.idinfo.pack(side=LEFT)
        self.b1.pack(side=RIGHT)

        # Container 3: Nome
        self.cont3 = Frame(master, padx=30)
        self.cont3.pack()
        self.Nome = Label(self.cont3, text="Nome:", font=self.fontep, padx=-20)
        self.idnome = Entry(self.cont3, width=27)
        self.Nome.pack(side=LEFT)
        self.idnome.pack(side=LEFT)

        # Container 4: Telefone
        self.cont4 = Frame(master, padx=30)
        self.cont4.pack()
        self.tel = Label(self.cont4, text="Telefone:", font=self.fontep, padx=-20)
        self.idtel = Entry(self.cont4, width=24)
        self.tel.pack(side=LEFT)
        self.idtel.pack(side=LEFT)

        # Container 5: E-mail
        self.cont5 = Frame(master, padx=30)
        self.cont5.pack()
        self.email = Label(self.cont5, text="E-mail:", font=self.fontep, padx=-20)
        self.idema = Entry(self.cont5, width=26)
        self.email.pack(side=LEFT)
        self.idema.pack(side=LEFT)

        # Container 6: Usuário
        self.cont6 = Frame(master, padx=30)
        self.cont6.pack()
        self.usuario = Label(self.cont6, text="Usuario:", font=self.fontep, padx=-20)
        self.idusa = Entry(self.cont6, width=25)
        self.usuario.pack(side=LEFT)
        self.idusa.pack(side=LEFT)

    def buscar_usuario(self):
        id_usuario = self.idinfo.get()
        usuario = Usuarios.buscar_por_id(
            id_usuario)  # Assumindo que você tenha um método buscar_por_id na classe Usuarios

        if usuario:
            self.idnome.delete(0, END)
            self.idnome.insert(0, usuario.nome)
            self.idtel.delete(0, END)
            self.idtel.insert(0, usuario.telefone)
            self.idema.delete(0, END)
            self.idema.insert(0, usuario.email)
            self.idusa.delete(0, END)
            self.idusa.insert(0, usuario.usuario)
        else:
            # Caso o usuário não seja encontrado, limpar os campos
            self.idnome.delete(0, END)
            self.idtel.delete(0, END)
            self.idema.delete(0, END)
            self.idusa.delete(0, END)
            # Aqui você poderia adicionar uma mensagem de erro, por exemplo usando messagebox


# Uso
root = tk.Tk()
app = Busca(master=root)
root.mainloop()
