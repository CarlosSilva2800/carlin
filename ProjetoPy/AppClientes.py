from clientes import Clientes  # Assuming you have a Clientes class similar to Usuarios
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        # Containers for organizing widgets
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        # Title Label
        self.titulo = Label(self.container1, text="Informe os dados do cliente:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        # ID Cliente
        self.lblidcliente = Label(self.container2, text="idCliente:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)

        self.txtidcliente = Entry(self.container2)
        self.txtidcliente["width"] = 10
        self.txtidcliente["font"] = self.fonte
        self.txtidcliente.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCliente
        self.btnBuscar.pack(side=RIGHT)

        # Nome Cliente
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        # Telefone Cliente
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        # Email Cliente
        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        # Endereço Cliente
        self.lblendereco = Label(self.container6, text="Endereço:", font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)

        self.txtendereco = Entry(self.container6)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        # Data de Nascimento Cliente
        self.lbldatanascimento = Label(self.container7, text="Data Nasc.:", font=self.fonte, width=10)
        self.lbldatanascimento.pack(side=LEFT)

        self.txtdatanascimento = Entry(self.container7)
        self.txtdatanascimento["width"] = 25
        self.txtdatanascimento["font"] = self.fonte
        self.txtdatanascimento.pack(side=LEFT)

        # Botões de Ação
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCliente
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCliente
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCliente
        self.bntExcluir.pack(side=LEFT)

    # Placeholder methods to be implemented
    def buscarCliente(self):
        # Code to search for a client by ID
        pass

    def inserirCliente(self):
        # Code to insert a new client
        pass

    def alterarCliente(self):
        # Code to update client data
        pass

    def excluirCliente(self):
        # Code to delete a client
        pass


# Example usage:
if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()