from AlavancaAcionamento import AlavancaAcionamento
from ValvulaAlimentacao import ValvulaAlimentacao
from ComportaVedacao import ComportaVedacao

class CaixaAcoplada(object):
    def __init__(self):
        print("Construtor da caixa do vaso sanitário")
        self.alavanca = AlavancaAcionamento()
        #self.valvula = ValvulaAlimentacao()
        #self.comporta = ComportaVedacao()
        #self.nivel_Maximo = 6.0
        #self.nivel_Agua = 0
        #self.encher_Caixa()

    def __del__(self):
        print(f"Removendo caixa acoplada: endereço {id(self)}")


    def acionar(self,opcao=None):
        print("Acionando o vaso sanitário")
        if type(opcao) == int:
            if opcao == 1:
                print("Número 1. Gastar pouca água")
                self.alavanca.acionar(opcao)
                #self.comporta.abrir()
                #self.nivel_Agua = self.nivel_Maximo/2
                #self.comporta.fechar()
                #self.valvula.encher_Agua()
                #self.encher_Caixa()
            elif opcao == 2:
                print("Número 2. ")
                self.alavanca.acionar(opcao)
                #self.comporta.abrir()
                #self.nivel_Agua = 0
                #self.comporta.fechar()
                #self.valvula.encher_Agua()
                #self.encher_Caixa()
            else:
                print("Opção desconhecida")
        else:
            print("Não é o vaso inteligente...")
            self.alavanca.acionar()
            #self.comporta.abrir()
            #self.nivel_Agua = 0
            #self.comporta.fechar()
            #self.valvula.encher_Agua()
            #self.encher_Caixa()

    def Relatorio(self):
        self.alavanca.Relatorio()
