class ValvulaAlimentacao():
    def __init__(self):
        print("Construtor da válvula de alimentação")
        self.capacidade_Vazao = 1.1
        self.nivel_Maximo = 6.0
        self.nivel_Agua = 0
        self.encher_Caixa()
    def __del__(self):
        print(f"Removendo válvula de alimentação: endereço {id(self)}")

    def encher_Caixa(self):
        print("Encher a caixa d'agua.")
        while self.nivel_Agua < self.nivel_Maximo:
            self.nivel_Agua = self.nivel_Agua + self.get_Vazao()
            if self.nivel_Agua > self.nivel_Maximo:
                self.nivel_Agua = self.nivel_Maximo
            print(f"Nível de água: {round(self.nivel_Agua,2)}")

        print(f"Vazão: {self.capacidade_Vazao} litros/seg")
    def get_Vazao(self):
        return self.capacidade_Vazao