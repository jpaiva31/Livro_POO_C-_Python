from Pizza import pizza
def mostrarCardapio():
    print("""Bem vindo(a) à pizzaria do Paivote
    ---------SABORES--------
    SABOR DA PIZZA               VALORES 

1   Frango com catupiry        P-34.80 | M-40.80 | G-47.40

2   Frango com cheddar         P-35.20 | M-41.20 | G-47.80

3   Frango com molho barbecue  P-34.20 | M-40.20 | G-46.80

4   Peito de peru              P-34.20 | M-40.20 | G-46.80

5   Peito de peru com catupiry P-37.20 | M-43.20 | G-49.80""")

def mostraIgredientes():
    print("""---------SABORES--------
        SABOR DA PIZZA               IGREDIENTES 

    1   Frango com catupiry         Molho de tomate natural, frango desfiado ricamente            
                                    temperado, legítimo catuppiry, azeitonas graúdas e orégano.
                                    Se desejar, você pode trocar a massa tradicional pela massa
                                    100% farinha integral.

    2   Frango com cheddar          Molho de tomate natural, frango desfiado ricamente temperado
                                    cheddar, cobertura de batata palha, azeitonas graúdas e orégano.                  35.20,41.20,47.80
                                    Se desejar, você pode trocar a massa tradicional pela massa 100%
                                    farinha integral

    3   Frango com molho barbecue   Molho de tomate natura, mussarela, frango desfiado ricamente temperado,
                                    milho verde, molho barbecue, azeitonas graúdas e orégano.
                                    Se desejar, você pode trocar a massa tradicional pela massa 100%
                                    farinha integral

    4   Peito de peru               Molho de tomate natura, mussarela, fpeito de peru,mussarela
                                    se desejar, você pode trocar a massa tradicional pela massa 100%
                                    farinha integral

    5   Peito de peru com catupiry  Molho de tomate natural, mussarela, peito de peru, legitimo catupiry,
                                    azeitonas graúdas e orégano. Você pode trocar a massa tradicional pela massa 100%
                                    farinha integral""")
def calcPreco(lista):
    precoTot = 0
    for c in lista:
        precoTot+=c.getPreco()
    return precoTot


def carrinho(lista):
    for c in lista:
        print(f"{c.getNome()}   R$ {c.getPreco()}")

    print(f"Preço tot: {calcPreco(lista)}")

pedidos = []
a = ' '
while a not in 'Nn':
    mostrarCardapio()
    b= int(input("""O que você deseja?
1-Comprar pizza
2-Mostrar igredientes
3-Mostrar carrinho
4-Sair
"""))
    if b == 4:
        break
    if b == 1:
        sabor2=' '
        mostrarCardapio()
        sabor1 = int(input("Qual sabor você quer?"))
        sabor2 = str(input("Deseja mais algum sabor?[S/N]"))
        if sabor2 in 'Ss':
            mostrarCardapio()
            sabor2 = int(input("Qual o segundo sabor da sua pizza?"))
        else:
            sabor2 = 0
        tamanho = str(input("Qual tamanho da sua pizza? [P/M/G]"))
        if tamanho in "PpMmGg":
            if tamanho in "Pp":
                tamanho = 0
            elif tamanho in "Mm":
                tamanho = 1
            elif tamanho in "Gg":
                tamanho = 2
        if sabor2 == 0:
            aux = pizza(tamanho, sabor1)
            pedidos.append(aux)
        else:
            print(f"Tamanho: {tamanho}")
            aux = pizza(tamanho,sabor1, sabor2)
            pedidos.append(aux)
    if b == 2:
        mostraIgredientes()
    if b == 3:
        carrinho(pedidos)
