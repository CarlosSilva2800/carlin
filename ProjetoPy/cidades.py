from Banco import Banco

class Cidades(object):
    def __init__(self, idcidade = 0, nome = "", estado = "", pais = ""):
        self.info = {}
        self.idcidade = idcidade
        self.nome = nome
        self.estado = estado
        self.pais = pais

    def insertCity(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_cidades (nome, estado, pais) VALUES ('" + self.nome + "', '" +
            self.estado + "', '" + self.pais + "')")
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da cidade"

    def updateCity(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_cidades SET nome = '" + self.nome + "', estado = '" + self.estado +
            "', pais = '" + self.pais +
            "' WHERE idcidade = " + str(self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da cidade"

    def deleteCity(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE idcidade = " + str(self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da cidade"

    def selectCity(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE idcidade = " + str(idcidade))
            for linha in c:
                self.idcidade = linha[0]
                self.nome = linha[1]
                self.estado = linha[2]
                self.pais = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da cidade"