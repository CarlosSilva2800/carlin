from cidades import Cidades
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        # Containers para layout
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

        # Título
        self.titulo = Label(self.container1, text="Informe os dados da cidade:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        # ID Cidade
        self.lblidcidade = Label(self.container2, text="ID Cidade:", font=self.fonte, width=10)
        self.lblidcidade.pack(side=LEFT)
        self.txtidcidade = Entry(self.container2)
        self.txtidcidade["width"] = 10
        self.txtidcidade["font"] = self.fonte
        self.txtidcidade.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarCidade)
        self.btnBuscar.pack(side=RIGHT)

        # Nome da Cidade
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        # Estado
        self.lblestado = Label(self.container4, text="Estado:", font=self.fonte, width=10)
        self.lblestado.pack(side=LEFT)
        self.txtestado = Entry(self.container4)
        self.txtestado["width"] = 25
        self.txtestado["font"] = self.fonte
        self.txtestado.pack(side=LEFT)

        # País
        self.lblpais = Label(self.container5, text="País:", font=self.fonte, width=10)
        self.lblpais.pack(side=LEFT)
        self.txtpais = Entry(self.container5)
        self.txtpais["width"] = 25
        self.txtpais["font"] = self.fonte
        self.txtpais.pack(side=LEFT)

        # Mensagem
        self.lblmensagem = Label(self.container9, text="", font=("Calibri", "8", "italic"))
        self.lblmensagem.pack()

        # Botões de ação
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.bntInsert.pack(side=LEFT)
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.bntAlterar.pack(side=LEFT)
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.bntExcluir.pack(side=LEFT)

    def buscarCidade(self):
        idcidade = self.txtidcidade.get()
        cidade = Cidades()
        cidade.selectCity(idcidade)
        self.txtnome.delete(0, END)
        self.txtestado.delete(0, END)
        self.txtpais.delete(0, END)
        if cidade.idcidade:
            self.txtnome.insert(0, cidade.nome)
            self.txtestado.insert(0, cidade.estado)
            self.txtpais.insert(0, cidade.pais)
            self.lblmensagem.config(text="Cidade encontrada com sucesso!")
        else:
            self.lblmensagem.config(text="Cidade não encontrada")

    def inserirCidade(self):
        cidade = Cidades(
            nome=self.txtnome.get(),
            estado=self.txtestado.get(),
            pais=self.txtpais.get()
        )
        resultado = cidade.insertCity()
        self.lblmensagem.config(text=resultado)

    def alterarCidade(self):
        cidade = Cidades(
            idcidade=self.txtidcidade.get(),
            nome=self.txtnome.get(),
            estado=self.txtestado.get(),
            pais=self.txtpais.get()
        )
        resultado = cidade.updateCity()
        self.lblmensagem.config(text=resultado)

    def excluirCidade(self):
        idcidade = self.txtidcidade.get()
        cidade = Cidades(idcidade=idcidade)
        resultado = cidade.deleteCity()
        self.lblmensagem.config(text=resultado)


# Executando a aplicação
if __name__ == "__main__":
    root = Tk()
    root.title("Gerenciamento de Cidades")
    app = Application(master=root)
    root.mainloop()