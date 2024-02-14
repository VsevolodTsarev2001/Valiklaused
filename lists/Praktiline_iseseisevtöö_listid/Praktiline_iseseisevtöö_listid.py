from string import * 
from random import *


##1
#vokaali=["a","e","u","o","i","ü","ö","ä"]
#konsonanti="qwrtpsdfghklzxcvbnmj"
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sõna või laus: ").lower() #"ABCD"->"abcd!"
#tekst_list=list(tekst) #["a","b","c","d","!"]
#for sümbol in tekst_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("Vokaali:",v)
#print("Konsonanti:",k)
#print("Kirjuvahemärgid:",m)
#print("Tühikud:",t)
##2

## Küsi kasutajalt viis nime
#nimed = []
#for i in range(5):
#    nimi = input("Sisestage nimi: ").capitalize()
#    nimed.append(nimi)
## Kuva nimed tähestikulises järjekorras
#print("Nimed tähestikulises järjekorras:")
#nimed.sort()
#print(nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#print("Vimasena oli lisatud: ", nimi)
## Lisa võimalus muuta loendis olevaid nimesid
#print("Kas soovite muuta loendis olevaid nimesid?")
#muuda = input("Jah või Ei: ")
#if muuda.lower() == "jah":
#    indeks = int(input("Sisestage muudetava nime indeks: "))
#    uus_nimi = input("Sisestage uus nimi: ")
#    nimed[indeks] = uus_nimi
#    print("Nimed pärast muutmist:", nimed)
##dublikatid1
#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)
##dublikat2
#uued_nimed=list(set(nimed))
##2.3
#vanused=[]
#for i in range(5):
#    vanus=int(input("Sisesta vanus: "))
#    vanused.append(vanus)
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=sum(vanused)
#print("Suurim vanus:", maksimum)
#print("Väikseim vanus:", minimum)
#print("Kogusumma:", summa)
#print("Keskmine vanus:", keskmine)
#for i in range(5):
#    print(nimed[i],"on ", vanused[i],"aastat vana")



##3
#arvud=[]
#N=int(input("Mitu rida joonistamine? "))
#S=input("Sisesta sümbol: ")
##loendi täitmine
#for p in range(N):
#    arvud.append(randint(1,100))
##diagrammi loomine
#for p in range(N):
#    print(arvud[p]*S)



#4
Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    while True:
        try:
            indeks=int(input("Sisesta oma indeks: "))
            indeks_elemendide_arv=len(str(indeks)) 
            if indeks_elemendide_arv==5:
                print("5numbriline indeks ")
                break
            else:
                print("On vaja 5numbriline arv(indeks)")
        except:
            print("Vale andmetüüp!")
    #arv1=indeks//10000
    #print(arv1)
    symbolid=list(str(indeks))
    sym1=symbolid[0]
    print(sym1)
    print(f"Sa elad piirkonnas {Indeksid[int(symbolid[0])-1]}")