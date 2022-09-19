from Politico import Politico
class Vereador(Politico):
    def __init__(self,nome,partido,municipio,estado):
        Politico.__init__(self)
        self.setNome(nome)
        self.setPartido(partido)
        self.set_Municipio(municipio)
        self.setEstado(estado)
        self.setFuncao("Propor leis municipais em benefício da população")
        self.setSalario(800)
    def set_Municipio(self,municipio):
        self.municipio = municipio
    def get_Municipio(self):
        return self.municipio
    def apresentacao(self):
        Politico.apresentacao(self)
        print(f'Sou vereador em {self.get_Municipio()}/{self.getEstado()} e meu suposto salário é R$ {self.getSalario()}')
