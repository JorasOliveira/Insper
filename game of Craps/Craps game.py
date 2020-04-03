import random

print("bem vindo ao jogo de Craps\nvamos comecar")
print("\nvoce tem 10,000 para apostar\n")
fichas = 10000
fase = 0


def comeOut(money):
    print("primeira fase: Come Out\n")
    dado1 = random.randrange(1, 6)
    dado2 = random.randrange(1, 6)
    soma = dado1 + dado2

def passLine(aposta, soma):
    if soma is 7:
        print("ganhou a aposta Pass Line!\n")
        return aposta * 2
    elif (soma is 2) or (soma is 3) or (soma is 12):
        print("perdeu a aposta Pass Line\n")
        return -aposta
    else:
        fase = 1
        print("agora vamos pra fase 2: Point\n")
        return None


def field(aposta, soma):
    if soma is 2:
        print("Voce Ganhou o dobro!!\n")
        return aposta + aposta*2
    if soma is 12:
        print("Voce Ganhou o triplo!!!\n")
        return aposta + aposta*3
    if soma is 3 or 4 or 9 or 11:
        print("ganhou a aposta Field!\n")
        return aposta * 2
    if soma is 5 or 6 or 7 or 8:
        print("perdeu a aposta Field\n")
        return -aposta
    # elif (dado1 or dado2) is 3 or 4 or 9 or 11:
    #     print("ganhou a aposta Field!\n")
    #     return aposta*2


comeOut(fichas)
print(passLine(5, 5))
print(field(5, 3))