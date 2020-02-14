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
 


if modo == 1:
    nomePlayer1 = input('Player, me diga seu nome: ')
    actPlayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomePlayer1)))

    for _ in range(3):
        actia1 = randint(1,3)

    print('     JO\n        KEN\n       PO')
