"author: Khalil Yassine"
from random import randint
import time
countjogador = 0
i = 1
print(" Seja bem vindo ao jokenpô mais diferenciado que você já viu")
time.sleep(1)
while i==1:
    print(""" Escolha sua opção:
        Papel = 1  Tesoura = 2  Pedra = 3  Spock = 4  Lagarto = 5 """)
    computador = randint (1,5)
    time.sleep(1)
    print("Me mostre que você é bom")
    time.sleep(1)
    jogador = int(input("Faça a sua escolha \n"))
    if computador == jogador-1:
         print ("Muito bem, você ganhou um ponto!")
         countjogador+=1
         time.sleep(1)
    elif jogador == 1 and computador == 3:
        print ("Muito bem, você ganhou um ponto!")
        countjogador+=1
        time.sleep(1)
    elif jogador == 2 and computador == 4:
        print ("Muito bem, você ganhou um ponto!")
        countjogador +=1
        time.sleep(1)   
    elif jogador == 3 and computador == 5 :
        print("Muito bem, você ganhou um ponto!")
        countjogador +=1
        time.sleep(1)
    elif jogador == 4 and computador == 1:
        print("Muito bem, você ganhou um ponto!")
        countjogador +=1
        time.sleep(1)
    elif jogador ==2 and computador ==5:
        print("Muito bem, você ganhou um ponto!")
        countjogador +=1
        time.sleep(1)
    elif jogador == 1 and computador == 5:
        print("Muito bem, você ganhou um ponto!")
        countjogador +=1
        time.sleep(1)
    elif jogador == computador:
        print("Empate")
        countjogador = 0
        time.sleep(1)
    else:
        countjogador
        print("Que pena, você perdeu um ponto!")
        countjogador = countjogador -1
    if countjogador == 3:
            time.sleep(1)
            print("Você venceu!!")
            i=0
            i=int(input("Para voltar a jogar digite 1 \n"))
    