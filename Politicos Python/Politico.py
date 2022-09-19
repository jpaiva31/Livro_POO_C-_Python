class Politico():
    def __init__(self):
        self.nome = ""
        self.partido = ""
        self.estado = ""
        self.funcao = ""
    def setNome(self,nome):
        self.nome=nome
    def setPartido(self,partido):
        self.partido = partido
    def setEstado(self,estado):
        self.estado = estado
    def setFuncao(self,funcao):
        self.funcao = funcao
    def getNome(self):
        return self.nome
    def getPartido(self):
        return self.partido
    def getEstado(self):
        return self.estado
    def getFuncao(self):
        return self.funcao
    def apresentacao(self):
        print(f'Olá, sou {self.getNome()}\nMeu partido é {self.getPartido()}')
