from ComportaVedacao import ComportaVedacao

class AlavancaAcionamento(object):
    def __init__(self):
        print("Construtor de alavanca de acionamento")
        self.contador1 = 0
        self.contador2 = 0
        self.comporta = ComportaVedacao()
    def __del__(self):
        print(f"Removendo alavanca: endereço {id(self)}")

    def acionar(self,opcao=None):
        print("Alavanca de acionamento ativada")
        self.comporta.abrir(opcao)
        if type(opcao) == int:
            if opcao == 1:
                self.contador1+=1
                self.comporta.valvula.nivel_Agua = self.comporta.valvula.nivel_Maximo / 2
            else:
                self.contador2+=1
                self.comporta.valvula.nivel_Agua = 0
        else:
            self.contador2+=1
            self.comporta.valvula.nivel_Agua = 0

    def Relatorio(self):
        print("Relatório de uso de água")
        print(f"Número de descargas Opção 1: {self.contador1}\nNúmero de descargas Opção 2: {self.contador2}")
