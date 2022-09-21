from Catupiry import catupiry
from Cheddar import cheddar
from Peito_Peru import peito_Peru
from Frango import frango
from Barbecue import barbecue

class pizza(catupiry, cheddar, frango,peito_Peru):
    def __init__(self,tam, sabor1,sabor2 = None):
        self.tam = tam
        if sabor1 == 1:
            self.sabor1 = frango()
            self.recheio1 = catupiry()
            self.preco1 = [34.8,40.80,47.40]
        if sabor1 == 2:
            self.sabor1 = frango()
            self.recheio1 = cheddar()
            self.preco1 = [35.2,41.20,47.80]
        if sabor1 == 3:
            self.sabor1 = frango()
            self.recheio1 = barbecue()
            self.preco1 = [34.2,40.20,46.80]
        if sabor1 == 4:
            self.sabor1 = peito_Peru()
            self.recheio1 = ' '
            self.preco1 = [34.2,40.20,46.80]
        if sabor1 == 5:
            self.sabor1 = peito_Peru()
            self.recheio1 = catupiry()
            self.preco1 = [37.2,43.20,49.80]
        if sabor2 == 1:
            self.sabor2 = frango()
            self.recheio2 = catupiry()
            self.preco2 = [34.8,40.80,47.40]
        if sabor2 == 2:
            self.sabor2 = frango()
            self.recheio2 = cheddar()
            self.preco2 = [35.2,41.20,47.80]
        if sabor2 == 3:
            self.sabor2 = frango()
            self.recheio2 = barbecue()
            self.preco2 = [34.2,40.20,46.80]
        if sabor2 == 4:
            self.sabor2 = peito_Peru()
            self.recheio2 = ' '
            self.preco2 = [34.2,40.20,46.80]
        if sabor2 == 5:
            self.sabor2 = peito_Peru()
            self.recheio2 = catupiry()
            self.preco2 = [37.2,43.20,49.80]
        self.setNome()


    def getSabor1(self):
        return self.sabor1.getSabor()
    def getSabor2(self):
        return self.sabor2.getSabor()
    def getPreco1(self, tam):
        return self.preco1[tam]
    def getPreco2(self, tam):
        return self.preco2[tam]
    def getTam(self):
        return self.tam
    def getPreco(self):
        return (self.getPreco1(self.getTam())+self.getPreco2(self.getTam()))/2
    def setNome(self):
        if self.recheio1 == ' ':
            self.nome = self.sabor1.getSabor()
        else:
            self.nome = self.sabor1.getSabor() + " com " + self.recheio1.getSabor()
        if self.sabor2 != None:
            self.nome += " e "
            if self.recheio2 == ' ':
                self.nome += self.sabor2.getSabor()
            else:
                self.nome += self.sabor2.getSabor() + " com " + self.recheio2.getSabor()
    def getNome(self):
        return self.nome
