import random
import sys
print("bem vindo ao jogo de Craps\nvamos comecar")
print("\nvoce tem 10,000 para apostar\n")
fichas = 10000  # quantidade dispoovinel para apostar
fase = 0  # marcador para a fase do jogo, 0 representa come out, 1 representa point
broke = 0  # marcador se o jogardor estiver sem fichas, sera usado para o loop do jogo
sum = 0  # variavel para que a fase point funcione direito
p = 0  # checa se acabamos de sair da pass line e fomos para a point, quando entrarmos na pass line p vira 1,
       # e dai vai se manter em 1 ate terminar a point e voltar para pass line, garantindo que os dados nao sejam rolados duplamente por rodada



# funcao para a aposta pass line
def passLine(aposta, soma):
    global fase
    global p
    if soma is 7:
        print("ganhou a aposta Pass Line!")
        return aposta * 2
    elif (soma is 2) or (soma is 3) or (soma is 12):
        print("perdeu a aposta Pass Line")
        return -aposta
    else:
        fase = 1
        print("agora vamos pra fase 2: Point")
        p = 0
        return None


# funcao para a fase point
def point(aposta, point, soma):
    global fase
    global p
    if soma is point:
        print("voce ganhou a fase point! Agora voltaremos para a Come Out")
        fase = 0
        p = 0
        return aposta * 2
    if soma is 7:
        print("voce perdeu a fase point, agora voltaremos para a Come Out")
        fase = 0
        p = 0
        return -aposta
    else:
        print("continuaremos na fase point")
        p = 1
        return aposta


# funcao para a aposta field
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


# funcao para a aposta any craps
def anyCraps(aposta, soma):
    if soma is 2 or soma is 3 or soma is 12:
        print("Parabens, voce ganhou a aposta Any Craps!")
        return aposta * 7
    else:
        print("voce perdeu a aposta Any Craps")
        return -aposta


# funcao para a aposta twelve
def twelve(aposta, soma):
    if soma is 12:
        print("parabens voce ganhou a aposta twelve!")
        return aposta * 30
    else:
        print("voce perdeu a aposta twelve")
        return - aposta


n = 1  # marcador do numero da rodada
#esse while loop executa o jogo em si, ele pergunta em sequencia qual aposta o jogador quer fazer, checa qual fase o jogo esta para deixar o jogador fazer apenas as apostas permitidas,
#tambem checa quantas fichas o jogador tem, e fala para ele
while broke != 1:
    dado1 = random.randrange(1, 6)
    dado2 = random.randrange(1, 6)
    soma = dado1 + dado2

    print("Estamos na rodada {0}".format(n))

    parar = input("se quiser parar de jogar, por favor digite 'y'")

    if parar is 'y':
        print("obrigado por jogar")
        sys.exit()

    if fichas is 0:  # se o jogador estiver sem fichas, o jogo acaba aqui :(
        broke = 1
        print("voce esta sem fichas, nao pode apostar mais, obrigado por jogar")
        sys.exit()

    if fase is 0:

        print("primeira fase: Come Out\n")
        pL = input("Quer apostar na aposta pass line? (y/n)")

        if pL is 'y':
            aposta = int(input("quanto quer apostar?"))
            h = passLine(aposta, soma)
            if h is not None:
                fichas += h

    if fase is 1:
        if p is 0:
            soma = sum
            dado1 = random.randrange(1, 6)
            dado2 = random.randrange(1, 6)
            soma = dado1 + dado2
            p = 1
            fichas += point(aposta, sum, soma)

        else:
            fichas += point(aposta, sum, soma)

    apostar = input("Quer fazer a aposta field? (y/n)")
    if apostar is 'y':
        aposta = int(input("quanto quer apostar?"))
        h = field(aposta, soma)
        if h is not None:
            fichas += h

    apostar = input("Quer fazer a any craps? (y/n)")
    if apostar is 'y':
        aposta = int(input("quanto quer apostar?"))
        h = anyCraps(aposta, soma)
        if h is not None:
            fichas += h


    apostar = input("Quer fazer a twelve? (y/n)")
    if apostar is 'y':
        aposta = int(input("quanto quer apostar?"))
        h = twelve(aposta, soma)
        if h is not None:
            fichas += h

    print("voce tem {0} fichas".format(fichas))
    n += 1


