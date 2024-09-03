import tkinter as tk


class Janela:
    def __init__(self, master=None):
        self.fontep = ("arial", "10", "bold")

        self.titulo = tk.Label(master)
        self.titulo["text"] = "busque"
        self.titulo["font"] = ("times new roman", "15", "bold")
        self.titulo.pack()

        self.cont2 = tk.Frame(master)
        self.cont2["padx"] = 30
        self.cont2.pack(side=tk.LEFT)
        self.b1 = tk.Button(self.cont2, text="Usuários", font=self.fontep)
        self.b1["width"] = 10
        self.b1.pack()

        self.cont3 = tk.Frame(master)
        self.cont3["padx"] = 30
        self.cont3.pack(side=tk.LEFT)
        self.b2 = tk.Button(self.cont3, text="Cidades", font=self.fontep)
        self.b2["width"] = 10
        self.b2.pack()

        self.cont4 = tk.Frame(master)
        self.cont4["padx"] = 30
        self.cont4.pack(side=tk.LEFT)
        self.b3 = tk.Button(self.cont4, text="Clientes", font=self.fontep)
        self.b3["width"] = 10
        self.b3.pack()

        self.cont5 = tk.Frame(master)
        self.cont5["padx"] = 8
        self.cont5.pack(side=tk.LEFT)
        self.b4 = tk.Button(self.cont5, text="fechar", font=self.fontep)
        self.b4["width"] = 5
        self.b4["command"] = master.quit  # Corrigido para fechar a janela
        self.b4.pack()


root = tk.Tk()
Janela(root)
root.mainloop()
