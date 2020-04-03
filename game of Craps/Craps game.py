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

def point(aposta, point, soma):
    if soma is point:
        print("voce ganhou a fase point! Agora voltaremos para a Come Out")
        return aposta * 2
    if soma is 7:
        print("voce perdeu a fase point, agora voltaremos para a Come Out")
        return -aposta
    else:
        print("continuaremos na fase point")
        return aposta


def passLine(aposta, soma):
    if soma is 7:
        print("ganhou a aposta Pass Line!")
        return aposta * 2
    elif (soma is 2) or (soma is 3) or (soma is 12):
        print("perdeu a aposta Pass Line")
        return -aposta
    else:
        fase = 1
        print("agora vamos pra fase 2: Point")
        return None


def field(aposta, soma):
    if soma is 2:
        print("Voce Ganhou o dobro!!")
        return aposta + aposta * 2
    if soma is 12:
        print("Voce Ganhou o triplo!!!")
        return aposta + aposta * 3
    if soma is 3 or soma is 4 or soma is 9 or soma is 11:
        print("ganhou a aposta Field!")
        return aposta * 2
    if soma is 5 or soma is 6 or soma is 7 or soma is 8:
        print("perdeu a aposta Field")
        return -aposta
    return None


def anyCraps(aposta, soma):
    if soma is 2 or soma is 3 or soma is 12:
        print("Parabens, voce ganhou a aposta Any Craps!")
        return  aposta * 7
    else:
        print("voce perdeu a aposta Any Craps")
        return -aposta

def twelve(aposta, soma):
    if soma is 12:
        print("parabens voce ganhou a aposta twelve!")
        return aposta * 30
    else:
        print("voce perdeu a aposta twelve")
        return - aposta


comeOut(fichas)
print(passLine(5, 5))
print(field(5, 8))
print(anyCraps(5, 8))
print(twelve(5, 12))