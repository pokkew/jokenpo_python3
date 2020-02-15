#projeto pedra papel e tesoura (pve/pvp)
from random import randint
import sys
import os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
actia1 = 0
actia2 = 0
actplayer1 = 0
actplayer2 = 0
pedra = 1
papel = 2
tesoura = 3
nomeplayer2 = 0
pa = 0
cont = 0
round = cont+1
contdraw = 0
contwinp1 = 0
contwinia1 = 0

print('\nPedra Papel e Tesoura, the game\n')
print('Selecionar modo de jogo: \n')
print('Player vs I.A: digite 1\n')
print('Player vs Player: digite 2\n')
print('I.A vs I.A: digite 3\n')
modo = int(input(''))

#Modo player vs I.A
if (modo == 1):
    nomeplayer1 = input('Player, me diga seu nome: ')
    while pa == 0:
        actplayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer1)))
        cont +=1
        for _ in range(3):
            actia1 = randint(1,3)#gera o valor aleatorio da IA

        print('     JO\n        KEN\n       PO')#tá torto, arrumar!
        if actplayer1 == actia1: #condições de empate
            contdraw +=1
            if actplayer1 == 1:
                print('{0} jogou ...\n PEDRA\nI.A também, empate.' .format(nomeplayer1))
            elif actplayer1 == 2:
                print('{0} jogou ...\n PAPEL\nI.A também, empate.'.format(nomeplayer1))
            elif actplayer1 == 3:
                print('{0} jogou ...\n TESOURA\nI.A também, empate.'.format(nomeplayer1))

        elif actplayer1 == 1 and actia1 == 3:#condições de vitora Player
            contwinp1 +=1
            print('{0} jogou ...\n PEDRA\nI.A jogou TESOURA'.format(nomeplayer1))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 2 and actia1 == 1:
            contwinp1 +=1
            print('{0} jogou ...\n PAPEL\nI.A jogou PEDRA'.format(nomeplayer1))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 3 and actia1 == 2:
            contwinp1 +=1
            print('{0} jogou ...\n TESOURA\n I.A jogou PAPEL'.format(nomeplayer1))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))

        elif actplayer1 == 3 and actia1 == 1:#condição de vitoria I.A
            contwinia1 +=1
            print('{0} jogou ...\n TESOURA\nI.A jogou PEDRA'.format(nomeplayer1))
            print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))
        elif actplayer1 == 1 and actia1 == 2:
            contwinia1 +=1
            print('{0} jogou ...\n PEDRA\nI.A jogou PAPEL'.format(nomeplayer1))
            print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))
        elif actplayer1 == 2 and actia1 == 3:
            contwinia1 +=1
            print('{0} jogou ...\n PAPEL\nI.A jogou TESOURA'.format(nomeplayer1))
            print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))

        else:
            print('Valor Inválido') #PLAYER RETARDADO QUE NÃO SABE DIGITAR 1 2 ou 3
        print('\nRodada {0}\n'.format(round))
        print('{0} tem {1} vitórias\nI.A tem {2} Vitórias\n'.format(nomeplayer1,contwinp1,contwinia1))
        print('{0} Empates\n'.format(contdraw))
        pa = int(input('Digite 0 para jogar novamente\nDigite 1 para voltar ao menu\n'))
    else:
        restart_program()
#modo player VS player
elif (modo == 2):
    nomeplayer1 = input('Player Um, me diga seu nome: ')
    nomeplayer2 = input('Player Dois, me diga seu nome: ')
    while pa == 0:
        actplayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer1)))
        actplayer2 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer2)))
        cont +=1

        print('     JO\n        KEN\n       PO')#tá torto, arrumar!
        if actplayer1 == actplayer2: #condições de empate
            contdraw +=1
            if actplayer1 == 1:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))
            elif actplayer1 == 2:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))
            elif actplayer1 == 3:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))

        elif actplayer1 == 1 and actplayer2 == 3:#condições de vitora Player
            contwinp1 +=1
            print('{0} jogou ...\n PEDRA\n{1} jogou TESOURA'.format(nomeplayer1))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 2 and actplayer2 == 1:
            contwinp1 +=1
            print('{0} jogou ...\n PAPEL\n{1} jogou PEDRA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 3 and actplayer2 == 2:
            contwinp1 +=1
            print('{0} jogou ...\n TESOURA\n {1} jogou PAPEL'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))

        elif actplayer1 == 3 and actplayer2 == 1:#condição de vitoria I.A
            contwinia1 +=1
            print('{0} jogou ...\n TESOURA\n{1} jogou PEDRA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))
        elif actplayer1 == 1 and actplayer2 == 2:
            contwinia1 +=1
            print('{0} jogou ...\n PEDRA\n{1} jogou PAPEL'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))
        elif actplayer1 == 2 and actplayer2 == 3:
            contwinia1 +=1
            print('{0} jogou ...\n PAPEL\n{1} jogou TESOURA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))

        else:
            print('Valor Inválido') #PLAYER RETARDADO QUE NÃO SABE DIGITAR 1 2 ou 3
        print('\nRodada {0}\n'.format(round))
        print('{0} tem {1} vitórias\n{3} tem {2} Vitórias\n'.format(nomeplayer1,contwinp1,contwinia1,nomeplayer2))
        print('{0} Empates\n'.format(contdraw))
        pa = int(input('Digite 0 para jogar novamente\nDigite 1 para voltar ao menu\n'))
    else:
        restart_program()

else:
    print('valor inválido')
    restart_program()