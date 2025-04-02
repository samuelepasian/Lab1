import random
from domanda import Domanda
from player import Player

def generaDomanda(lista, livello):
    domande=[]
    for elemento in lista:
        if isinstance(elemento, Domanda) and elemento.difficolta==livello:
            domande.append(elemento)
    if len(domande)==0:
        return None
    domanda=random.choice(domande)
    return domanda

def corretto(risposta, domanda, player):
    if isinstance(domanda,Domanda) and risposta==domanda.corretta[:-1 ]:
        player.punteggio+=1
        return True
    else:
        return False

def gioco(domande):
    nome=input("Inserisci nome giocatore ")
    player=Player(nome, 0)
    giusto = True
    difficolta=0
    while giusto==True:
        opzioni=[]
        domanda=generaDomanda(domande, difficolta)
        print(domanda.testo[:-1])
        opzioni.append(domanda.corretta)
        for elemento in domanda.errate:
            opzioni.append(elemento)
        random.shuffle(opzioni)
        for opzione in opzioni:
            print(opzione[:-1])
        risposta=input("Inserisci risposta ")
        giusto= corretto(risposta, domanda, player)
        if giusto==True:
            print("CORRETTO \n")
            difficolta+=1
        else:
            print("ERRATO \n")
            print(f"{player.nome} {player.punteggio}")

