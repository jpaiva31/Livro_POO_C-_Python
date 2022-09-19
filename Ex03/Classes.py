class Transporte:
    def mostrar(self):
        print('Transporte sendo apresentado')

class Caminhao(Transporte):
    def __init__(self,modelo=None):
        self.modelo=modelo

    def mostrar(self):
        print(f'Caminhao modelo {self.modelo}')

