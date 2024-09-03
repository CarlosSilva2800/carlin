import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para conectar ao banco de dados e buscar os dados
def fetch_data():
    try:
        conn = sqlite3.connect('banco.db')  # Conectando ao banco de dados
        cursor = conn.cursor()

        # Executando uma consulta SQL para pegar todos os dados da tabela
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()  # Buscando todos os resultados
        conn.close()
        return rows
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return []

# Função para popular a Treeview com os dados do banco
def populate_treeview(treeview, data):
    for row in data:
        treeview.insert("", "end", values=row)

# Configurando a interface principal
root = tk.Tk()
root.title("Exibindo Dados do Banco de Dados")

# Configurando a Treeview
columns = ("ID", "Nome", "Telefone", "Email")  # Definindo as colunas
treeview = ttk.Treeview(root, columns=columns, show='headings')

# Definindo as larguras das colunas
treeview.column("ID", width=50)
treeview.column("Nome", width=150)
treeview.column("Telefone", width=100)
treeview.column("Email", width=200)

for col in columns:
    treeview.heading(col, text=col)

# Adicionando um Scrollbar vertical
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=treeview.yview)
treeview.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

treeview.pack(fill=tk.BOTH, expand=True)

# Pegando os dados do banco e populando a Treeview
data = fetch_data()
populate_treeview(treeview, data)

# Iniciando a aplicação
root.mainloop()
