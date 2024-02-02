from random import *
from ssl import HAS_TLSv1
#1
while True:
    try:
        n=int(input("sisenda number vahemikkus 1-9:"))
        if 1 <= n <= 9:
            break
    except ValueError:
        print("Vale tüüp")

for _ in range(n):
    print("   ~~~~~   ", end="")
print()  # Liigu järgmisele reale

for _ in range(n):
    print("  /_____\\  ", end="")
print()

for _ in range(n):
    print("  | []  |  ", end="")
print()

for _ in range(n):
    print("   -----   ", end="")
print()
#2
N=25
kesk1=0
kesk2=0
for i in range(N):
    h1=randint(1,5)
    h2=randint(1,5)
    kesk1+=h1 
    kesk2+=h2 
kesk1/=N 
kesk2/=N 
print(f"Keskmine hinne 1 klassis on @{kesk1}")
print(f"Keskmine hinne 2 klassis on @{kesk2}")
#3
õpilased = 22
maksimaalne = 1
minimaalne = 5
for i in range(õpilased):
    hinned = randint(100, 500)/100
    print(hinned)
    if hinned > maksimaalne:
        maksimaalne = hinned
    if hinned < minimaalne:
        minimaalne = hinned
print("Maksimaalne hind on::", maksimaalne)
print("Minimaalne hind on:", minimaalne)
#4.1
#elanikkond = [120, 80, 150, 90, 110, 70, 130, 100, 140, 95, 120, 85] #tuhendetes inimesi
#pindala = [50, 30, 60, 40, 45, 25, 55, 35, 58, 38, 48, 33] # km^2

#kogu_tihendus = 0

#for i in range(len(elanikkond)):
#    tihedus = elanikkond[i] / pindala[i]
#    kogu_tihendus += tihedus

#keskmine_tihendus = kogu_tihendus / len(elanikkond)

#print(f"Piirkonna keskmine rahvastiku tihedus: {keskmine_tihendus} tuhat inimest/km^2")

#4.2
sum_num=0
sum_km=0
for i in range(12):
    num=randint(1000,100000)
    km=randint(1,1000)
    sum_num+=num
    sum_km+=km 
    print(f"{i+1}. maakond. \nElanikud: {num}. Pindala: {km}\n Kokku:{sum_num},{sum_km}")
vastus=sum_num/sum_km
print(f"Keskmine: {vastus:.3f}")





#4 вариант 5 задача
while True:
    try:
        K=int(input("Mitu kotleti sul on? "))
        if K>0:break
    except ValueError:
        print("Vale tüüp")
while True:
    try:
        M=int(input("Mitu kotleti ühel pannil? "))
        if M>0:break
    except ValueError:
        print("Vale tüüp")
pann=0
lisapann=0
while K>0:
    if K>=M:
        K-=M
        pann+=1
        print(f"Praetud: {pann} tk")
    elif K<M:
        lisapann+=1
        print(f"Praetud: {lisapann} tk")
        break
print(f"Täispannid: {pann} ja veel on vaja {lisapann}")