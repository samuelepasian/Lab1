from domanda import Domanda
import game

domande=[]
count=0
nriga=0
domanda=Domanda()
with open ("domande.txt","r") as file:
    righe=file.readlines()
    while count<len(righe):
        if righe[count]=="\n":
            domande.append(domanda)
            domanda=Domanda()
            domanda.errate=[]
            nriga=-1
        match nriga:
            case 0: domanda.testo=righe[count]
            case 1: domanda.difficolta=int(righe[count])
            case 2: domanda.corretta= righe[count]
        if nriga>2:
            domanda.errate.append(righe[count])
        nriga+=1
        count+=1

game.gioco(domande)







