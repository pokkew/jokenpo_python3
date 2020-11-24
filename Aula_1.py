#projeto pedra papel e tesoura (pve/pvp)
from random import randint
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def decide_vencedor(x,y, dic_vic):
    r = {}
    if x == y:
        r["resultado"] = "empate"
        dic_vic["empate"] = int(dic_vic["empate"]) + 1
    elif x==1 and y==2:
        r["resultado"] = "y"
        dic_vic["ai"] = int(dic_vic["ai"]) + 1
    elif x==1 and y==3:
        r["resultado"] = "x"
        dic_vic["player"] = int(dic_vic["player"]) + 1
    elif x==2 and y==1:
        r["resultado"] = "x"
        dic_vic["player"] = int(dic_vic["player"]) + 1
    elif x==2 and y==3:
        r["resultado"] = "y"
        dic_vic["ai"] = int(dic_vic["ai"]) + 1
    elif x==3 and y==1:
        r["resultado"] = "y"
        dic_vic["player"] = int(dic_vic["player"]) + 1
    elif x==3 and y==2:
        r["resultado"] = "x"
        dic_vic["ai"] = int(dic_vic["ai"]) + 1
    return r,dic_vic

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

dicVic = {"player":0, "ai":0, "empate":0 }
jogadas ={"player1": "", "player2": "", "ai": "" }

print('\nPedra Papel e Tesoura, the game\n')
print('Selecionar modo de jogo: \n')
print('Player vs I.A: digite 1\n')
print('Player vs Player: digite 2\n')
modo = int(input(''))

#Modo player vs I.A
if (modo == 1):
    nomeplayer1 = input('Player, me diga seu nome: ')
    while pa == 0:
        actplayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer1)))
        if actplayer1 == 1:
            jogadas["player1"] = "pedra"
        elif actplayer1 == 2:
            jogadas["player1"] = "papel"
        if actplayer1 == 3:
            jogadas["player1"] = "tesoura"
        cont +=1
        for _ in range(3):
            actia1 = randint(1,3)#gera o valor aleatorio da IA
        if actia1 == 1:
            jogadas["ai"] = "pedra"
        elif actia1 == 2:
            jogadas["ai"] = "papel"
        if actia1 == 3:
            jogadas["ai"] = "tesoura"

        print("==================================================================")
        print('JO\n\tKEN\n\t\tPO')#tá torto, arrumar!
        resultado, dicVic = decide_vencedor(actplayer1, actia1, dicVic)
        print(f"{nomeplayer1} jogou ...\n {jogadas['player1'].upper()}")
        print(f"ai jogou ...\n {jogadas['ai'].upper()}")
        if resultado["resultado"] == "empate": 
            print("Empate !!!")
        elif resultado["resultado"] == "x": 
            print("Vitória do jogador !!!")
        elif resultado["resultado"] == "y": 
            print("Vitória da AI !!!")

        print(f"{nomeplayer1} tem {dicVic['player']} vitória(s)")
        print(f"AI tem {dicVic['ai']} vitória(s)")
        print(f"{dicVic['empate']} Empate(s)")
        print("==================================================================")

        # print("#########################OLD CODE #########################")
        # if actplayer1 == actia1: #condições de empate
        #     contdraw +=1
        #     if actplayer1 == 1:
        #         print('{0} jogou ...\n PEDRA\nI.A também, empate.' .format(nomeplayer1))
        #     elif actplayer1 == 2:
        #         print('{0} jogou ...\n PAPEL\nI.A também, empate.'.format(nomeplayer1))
        #     elif actplayer1 == 3:
        #         print('{0} jogou ...\n TESOURA\nI.A também, empate.'.format(nomeplayer1))

        # elif actplayer1 == 1 and actia1 == 3:#condições de vitora Player
        #     contwinp1 +=1
        #     print('{0} jogou ...\n PEDRA\nI.A jogou TESOURA'.format(nomeplayer1))
        #     print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        # elif actplayer1 == 2 and actia1 == 1:
        #     contwinp1 +=1
        #     print('{0} jogou ...\n PAPEL\nI.A jogou PEDRA'.format(nomeplayer1))
        #     print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        # elif actplayer1 == 3 and actia1 == 2:
        #     contwinp1 +=1
        #     print('{0} jogou ...\n TESOURA\n I.A jogou PAPEL'.format(nomeplayer1))
        #     print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))

        # elif actplayer1 == 3 and actia1 == 1:#condição de vitoria I.A
        #     contwinia1 +=1
        #     print('{0} jogou ...\n TESOURA\nI.A jogou PEDRA'.format(nomeplayer1))
        #     print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))
        # elif actplayer1 == 1 and actia1 == 2:
        #     contwinia1 +=1
        #     print('{0} jogou ...\n PEDRA\nI.A jogou PAPEL'.format(nomeplayer1))
        #     print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))
        # elif actplayer1 == 2 and actia1 == 3:
        #     contwinia1 +=1
        #     print('{0} jogou ...\n PAPEL\nI.A jogou TESOURA'.format(nomeplayer1))
        #     print('{0}... derrota, mais sorte na proxima!'.format(nomeplayer1))

        else:
            print('Escolha inválida, ninguém leva ponto') #PLAYER RETARDADO QUE NÃO SABE DIGITAR 1 2 ou 3
        
        print('\n{0} tem {1} vitórias\nI.A tem {2} Vitórias'.format(nomeplayer1,contwinp1,contwinia1))
        print('{0} Empates\n'.format(contdraw))
        pa = int(input('Digite 0 para jogar novamente\nDigite 1 para voltar ao menu\nDigite 3 para sair do jogo\n  '))

    else:
        if pa == 1:
            restart_program()
        else:
            exit
#modo player VS player
elif (modo == 2):
    nomeplayer1 = input('Player Um, me diga seu nome: ')
    nomeplayer2 = input('Player Dois, me diga seu nome: ')
    while pa == 0:
        actplayer1 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer1)))
        actplayer2 = int(input('{0} escolha entre pedra, papel e tesoura: 1, 2 ou 3 respectivamente \n'.format(nomeplayer2)))

        print('     JO\n        KEN\n       PO')#tá torto, arrumar!
        if actplayer1 == actplayer2: #condições de empate
            contdraw +=1
            cont +=1
            if actplayer1 == 1:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))
            elif actplayer1 == 2:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))
            elif actplayer1 == 3:
                print('{0} jogou ...\n PEDRA\n{1} também, empate.' .format(nomeplayer1,nomeplayer2))

        elif actplayer1 == 1 and actplayer2 == 3:#condições de vitora Player
            contwinp1 +=1
            cont +=1
            print('{0} jogou ...\n PEDRA\n{1} jogou TESOURA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 2 and actplayer2 == 1:
            contwinp1 +=1
            cont +=1
            print('{0} jogou ...\n PAPEL\n{1} jogou PEDRA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))
        elif actplayer1 == 3 and actplayer2 == 2:
            contwinp1 +=1
            cont +=1
            print('{0} jogou ...\n TESOURA\n {1} jogou PAPEL'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer1))

        elif actplayer1 == 3 and actplayer2 == 1:#condição de vitoria I.A
            contwinia1 +=1
            cont +=1
            print('{0} jogou ...\n TESOURA\n{1} jogou PEDRA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))
        elif actplayer1 == 1 and actplayer2 == 2:
            contwinia1 +=1
            cont +=1
            print('{0} jogou ...\n PEDRA\n{1} jogou PAPEL'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))
        elif actplayer1 == 2 and actplayer2 == 3:
            contwinia1 +=1
            cont +=1
            print('{0} jogou ...\n PAPEL\n{1} jogou TESOURA'.format(nomeplayer1,nomeplayer2))
            print('{0}, parabéns, esse round é seu!'.format(nomeplayer2))

        else:
            print('Escolha inválida, ninguém leva ponto') #PLAYER RETARDADO QUE NÃO SABE DIGITAR 1 2 ou 3

        print('\n{0} tem {1} vitórias\n{3} tem {2} Vitórias'.format(nomeplayer1,contwinp1,contwinia1,nomeplayer2))
        print('{0} Empates\n'.format(contdraw))
        pa = int(input('Digite 0 para jogar novamente\nDigite 1 para voltar ao menu\nDigite 3 para sair do jogo\n'))

    else:
        if pa == 1:
            restart_program()
        else:
            exit

else:
    print('valor inválido, escolha entre as opções descritas')
    restart_program()