from datetime import *
from random import *


#10 практических заданий по теме Циклы


#1
#for
r=0
for i in range(15):
    arv=float(input("Sisesta {0}.arv".format(i+1)))
    if arv==int(arv):
        r+=1
print("Täisarvude arv on "+str(r))

#while True
r=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        r+=1
    if i==15: break
print("Täisarvude arv on "+str(r))

#while tingimustega
r=0
i=0
while i<15:
    i+=1
    arv=float(input("Sisesta {0}.arv ".format(i)))
    if arv==int(arv):
        r+=1
print("Täisarvude arv on "+str(r))


#2
#for
A=int(input("Sisestage number A: "))
arv = 0
for i in range(1, A + 1):
    arv += i
print(f"Kõigi naturaalarvude summa alates 1 enne {A} (kasutades loop'i for): {arv}")

#while True
A = int(input("Sisestage number A: "))
arv = 0
i = 1
while True:
    arv += i
    i += 1
    if i > A:
        break
print(f"Kõigi naturaalarvude summa alates 1 enne {A} (kasutades loop'i while True): {arv}")

#while
A = int(input("Sisestage number A: "))
arv = 0
i = 1
while i <= A:
    arv += i
    i += 1
print(f"Kõigi naturaalarvude summa alates 1 enne {A} (kasutades loop'i while): {arv}")

#3
#for
product_for = 1
for i in range(8):
    num = float(input("Sisestage number: "))
    if num > 0:
        product_for *= num
print(f"Positiivsete arvude korrutis: {product_for}")

#while True
product_while_true = 1
count = 0
while True:
    num = float(input("Sisestage number: "))
    if num > 0:
        product_while_true *= num
        count += 1
    if count == 8:
        break
print(f"Positiivsete arvude korrutis: {product_while_true}")

#while
product_while = 1
count = 0

while count < 8:
    num = float(input("Sisestage number: "))
    if num > 0:
        product_while *= num
        count += 1
print(f"Positiivsete arvude korrutis: {product_while}")


##14
#maht=int(input("Bussi maht: "))
#i=int(input("Inimeste arv: "))
#ba=round(i/maht) #2,3->2
#if i%maht!=0:
#    ba+=1
#vb=i%maht
#print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))



##1 Juku lähed kinno
#nimi=input("Mis on sinu nimi?").capitalize()  #"anna"->"Anna"
#print("Tere",nimi) #"Tere, Anna"
#if nimi=="Juku":
#    print("Lahme kinno")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>100:
#        pilet="vale vanus"
#    elif vanus<6:
#        pilet="tasuta"
#    elif vanus<=14:   #<15
#        pilet="lastepilet"
#    elif vanus<=65:
#        pilet="täispilet"
#    elif vanus<=100:
#        pilet="sooduspilet"
#    print(pilet) #Ilus ja õige vastus!"Vale vanus" või "On vaja osta...."
#else:
#    print("Ma ootan Jukut")
#print()




#protsent=randint(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"
#print(protsent,"% on testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif 0<protsent<60: #protsent>0 and protsent<60, protsent<60
#    tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsent<90:
#    tulemus="hinne 4"
#else:     #elif 90<=protsent<=100:
#    tulemus="hinne 5"
#print(tulemus)
#print()

#arv=randint(0,100) #juhuslik täisarv vahemikust 0...100

#print(arv) 
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()

#print("Tund on alanud")
#hilinemine=input("Kas õpilane on hilinenud?")
## "JAH"-a.upper(), "jah"-a.lower, "Jah"-a.capitalize(), jAH
#if hilinemine.capitalize()=="Jah":
#    print("Õpilane ootab 30 min")
#print("Õpilane astub klassi")

#2
# import random
# nimed = choice(["Kirill", "Bogdan", "Seva", "Gleb", "Martin", "Lev", "Sasha", "Elena", "Eva", "Mike", "Oleg", "Gena"])
# valitud_nimed = random.sample(nimed, len(nimed))
#
#
#
# print(f"Täna sinu pinginaaber on {nimed}!")

#3
# arv1 = int(input("Sisestage ruumi esimese seina pikkus (sentimeetrites): "))
# arv2 = int(input("Sisestage ruumi teise seina pikkus (sentimeetrites): "))
#
# S = arv1 * arv2
# P = 2*(arv1 + arv2)
# print("Периметр комнаты =", round(S, 2),"\n Ja ruumi pindala =", round(P, 2))
#
# remont = input("Kas soovite renoveerida? ")
# if remont.capitalize() == "Ja":
#     print(input("Kui palju maksab põranda asendamine ruutmeetri kohta?? "))

#4
# alghind = randint(0, 1000)
# print(alghind)
# if alghind >= 700:
#     soodus_protsentides = 30
#     allahindlus = (soodus_protsentides/ 100) * 30
#     uus_hind = alghind - allahindlus
#     print(f"Uus hind pärast 30% allahindlust on: {uus_hind}", )
# else:
#     print("Tootesoodustus algab 700€-st, seega 30% allahindlust ei saa")

#5
# temperatuur = randint(1, 20)
# print(temperatuur)
# if temperatuur >= 18:
#     print("Temperatuur on üle 18 kraadi, mis on soovitav toasoojus talvel.")
# else:
#     print("Temperatuur on 18 kraadi või madalam, soovitav on hoida soojem temperatuur talvel.")

#6
# pikkus= int(input("Mis on sinu pikkus?: "))
# print("Sa oled", pikkus)
# if 150 <= pikkus < 168:
#     pikkasvu = "lühike"
# elif 169 <= pikkus < 177:
#     pikkavu = "keskmine"
# else:
#     pikkasvu = "pikk"
# print(f'Sa oled {pikkasvu}')
            
#7
# pikkus = randint(140, 210)
# print(pikkus)
# sugu = choice(['mees', 'näine'])
# print(sugu)
# if sugu.lower() == 'mees':
#     if pikkus < 165:
#         print("Sa oled lühike mees.")
#     elif 165 <= pikkus < 180:
#         print("Sa oled keskmise pikkusega mees.")
#     else:
#         print("Sa oled pikk mees.")
# elif sugu.lower() == 'naine':
#     if pikkus < 155:
#         print("Sa oled lühike naine.")
#     elif 155 <= pikkus < 170:
#         print("Sa oled keskmise pikkusega naine.")
#     else:
#         print("Sa oled pikk naine.")
# else:
#     print("Palun sisestage kehtiv sugu.")
           
#9
# kylg1 = int(input("Sisestage kujundi esimene külg (cm): "))
# kylg2 = int(input("sisestage kujundi teine külg (cm): "))
# if kylg1 == kylg2:
#     print("See on ruut!")
# else:
#     print("See ei ole ruut")
         
#11.1
# import datetime
#
# birthday = input("Sisestage oma sünnipäev (YYYY-MM-DD): ")
#
# birthday = datetime.datetime.strptime(birthday, "%Y.%m.%d")
# current_date = datetime.datetime.now()
# age = current_date.year - birthday.year
#
# if age % 10 == 0:
#     print("teie sünnipäev on tähtpäev")
# else:
#     print("teie sünnipäev ei ole tähtpäev")
##11.2
#ta=date.today().year
#sp=date(int(input("Sünniaasta")),int(input("Sümmikuu: ")),int(input("Sünnipäev"))).year
#if (ta-sp)%5==0:
#    print("Juubel")
#else:
#    print("Tavaline sünnipäev")


##8.2 Poes
#arve_nr=date.today()#datetime.now()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#for toode in ["Piim","Leib","Komm"]:
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad ost?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu?"))
#        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#        summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#while True:
#    raha=float(input("Maksa "+str(summa)+"\n"))
#    if raha==summa:
#        print("Tänan ostu eest!")
#        break
#    elif raha>summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veel"+str(summa))
#8.1 poes
#arve_nr=date.today()#datetime.now()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0

#toode="Piim"
#hind=randint(50,150)/100
#v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad ost?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Leib"
#hind=randint(90,300)/100
#v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad ost?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Kommid"
#hind=randint(600,1500)/100
#v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad ost?").lower()
#if v=="jah":
#    mitu=int(input("Mitu?"))
#    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#raha=float(input("Maksa "+str(summa)))
#if raha==summa:
#    print("Tänan ostu eest!")
#elif raha>summa:
#    print("Tänan ostu eest! Tagasi "+str(raha-summa))
#else:
#    print("Maksa veel"+str(summa-raha))