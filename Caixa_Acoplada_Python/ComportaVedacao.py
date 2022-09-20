from ValvulaAlimentacao import ValvulaAlimentacao

class ComportaVedacao(object):
    def __init__(self):
        print("Consrutor da comporta de vedação")
        self.status = "FECHADO"
        self.valvula = ValvulaAlimentacao()

    def __del__(self):
        print(f"Removendo comporta de vedação: endereço {id(self)}")

    def abrir(self,vazao=None):
        if vazao == None or vazao == 2:
            print("Comporta de vedação aberta. Saindo toda a água")
            self.valvula.nivel_Agua = 0
        else:
            print(f"Comporta aberta. Saindo {vazao} de água")
            self.valvula.nivel_Agua = self.valvula.nivel_Maximo/2
        self.fechar()

    def fechar(self):
        print("Comporta de vedação fechada")
        self.status = "FECHADO"
        self.valvula.encher_Caixa()