import random
print("bem vindo ao jogo de Craps\nvamos comecar")
print("\nvoce tem 10,000 para apostar")
fichas = 10000
fase = 0

def comeOut(money):
    print("primeira fase: Come Out")
    dado1 = random.randrange(1, 6)
    dado2 = random.randrange(1, 6)



def passLine(aposta, dado1, dado2):
    soma = dado1 + dado2
    if soma is 7:
        print("ganhou a aposta Pass Line!")
        return aposta*2
    elif (soma is 2) or (soma is 3) or (soma is 12):
        print("perdeu a aposta Pass Line")
        return -aposta
    else:
        fase = 1
        print("agora vamos pra fase 2: Point")
        return None