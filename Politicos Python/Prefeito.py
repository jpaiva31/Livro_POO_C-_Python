from Politico import Politico
class Prefeito(Politico):
    def __init__(self,nome,partido,municipio,estado):
        Politico.__init__(self)
        self.setNome(nome)
        self.setPartido(partido)
        self.set_Municipio(municipio)
        self.setEstado(estado)
        self.setFuncao("Administrar o IPTU visando o melhor para a cidade")
    def set_Municipio(self,municipio):
        self.municipio = municipio
    def get_Municipio(self):
        return self.municipio
    def apresentacao(self):
        Politico.apresentacao(self)
        print(f'Sou prefeito em {self.get_Municipio()}/{self.getEstado}')
