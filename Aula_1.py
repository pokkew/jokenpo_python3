#projeto pedra papel e tesoura (pve/pvp)
from random import randint
actia1 = 0
actia2 = 0
actplayer1 = 0
actplayer2 = 0
pedra = 1
papel = 2
tesoura = 3
print('\nPedra Papel e Tesoura, the game\n')
print('Selecionar modo de jogo: \n')
print('Player vs I.A: digite 1\n')
print('Player vs Player: digite 2\n')
print('I.A vs I.A: digite 3\n')
modo = int(input(''))

#Modo player vs I.A
if (modo == 1):
    nomePlayer1 = input('Player, me diga seu nome: ')
    actPlayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomePlayer1)))

    for _ in range(3):
        actia1 = randint(1,3)#gera o valor aleatorio da IA

    print('     JO\n        KEN\n       PO')#tá torto, arrumar!
    if actplayer1 == actia1: #condições de empate
        if actplayer1 == 1:
            print('{0} jogou ...\n PEDRA\n I.A também, empate.' .format(nomePlayer1))
        elif actPlayer1 == 2:
            print ('{0} jogou ...\n PAPEL\n I.A também, empate.'.format(nomePlayer1))
        elif actPlayer1 == 3:
            print ('{0} jogou ...\n TESOURA\n I.A também, empate.'.format(nomePlayer1))

    elif actPlayer1 == 1 and actia1 == 3:#condições de vitora Player
        print ('{0} jogou ...\n PEDRA\n I.A jogou TESOURA'.format(nomePlayer1))
        print ('{0}, parabéns, esse round é seu!'.format(nomePlayer1))
    elif actPlayer1 == 2 and actia1 == 1:
        print ('{0} jogou ...\n PAPEL\n I.A jogou PEDRA'.format(nomePlayer1))
        print ('{0}, parabéns, esse round é seu!'.format(nomePlayer1))
    elif actPlayer1 == 3 and actia1 == 2:
        print ('{0} jogou ...\n TESOURA\n I.A jogou PAPEL'.format(nomePlayer1))
        print ('{0}, parabéns, esse round é seu!'.format(nomePlayer1))

    elif actPlayer1 == 3 and actia1 == 1:#condição de vitoria I.A
        print ('{0} jogou ...\n TESOURA\n I.A jogou PEDRA'.format(nomePlayer1))
        print('{0} derrota, mais sorte na proxima!'.format(nomePlayer1))
    elif actPlayer1 == 1 and actia1 == 2:
        print ('{0} jogou ...\n PEDRA\n I.A jogou PAPEL'.format(nomePlayer1))
        print('{0} derrota, mais sorte na proxima!'.format(nomePlayer1))
    elif actPlayer1 == 2 and actia1 == 3:
        print ('{0} jogou ...\n PAPEL\n I.A jogou TESOURA'.format(nomePlayer1))
        print('{0} derrota, mais sorte na proxima!'.format(nomePlayer1))

    else:
        print('Valor Inválido'): #PLAYER RETARDADO QUE NÃO SABE DIGITAR 1 2 ou 3
else:
    print('valor inválido')