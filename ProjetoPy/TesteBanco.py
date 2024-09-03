import sqlite3


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        c = self.conexao.cursor()

        # Criar tabela de usuários
        c.execute("""
        CREATE TABLE IF NOT EXISTS tbl_usuarios(
            idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT
        )
        """)

        # Criar tabela de cidades
        c.execute("""
        CREATE TABLE IF NOT EXISTS tbl_cidades(
            idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            estado TEXT
        )
        """)

        # Criar tabela de clientes
        c.execute("""
        CREATE TABLE IF NOT EXISTS tbl_clientes(
            idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            idcidade INTEGER,
            FOREIGN KEY(idcidade) REFERENCES tbl_cidades(idcidade)
        )
        """)

        self.conexao.commit()
        c.close()
