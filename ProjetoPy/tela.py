import tkinter as tk
from tkinter import ttk
import sqlite3


# Função para conectar ao banco de dados e buscar os dados
def fetch_data():
    try:
        conn = sqlite3.connect('banco.db')  # Conectando ao banco de dados
        cursor = conn.cursor()

        # Executando uma consulta SQL para pegar todos os dados da tabela
        cursor.execute("SELECT * FROM tbl_usuarios")
        rows = cursor.fetchall()  # Buscando todos os resultados
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        rows = []
    finally:
        if conn:
            conn.close()

    return rows


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
for col in columns:
    treeview.heading(col, text=col)

treeview.pack(fill=tk.BOTH, expand=True)

# Pegando os dados do banco e populando a Treeview
data = fetch_data()
populate_treeview(treeview, data)

# Iniciando a aplicação
root.mainloop()
