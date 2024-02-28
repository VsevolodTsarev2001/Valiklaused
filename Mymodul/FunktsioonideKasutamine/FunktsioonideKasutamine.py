from module1 import * #Summa as s



#(5)
a=float(input("sisestage a raha: "))
aasta=int(input("Sisestage kui palju aastaks: "))

print("teie tagastatud summa on: ",pank(a,aasta))




#(7)
paev=int(input("kirjutage paeva: "))
kuu=int(input("kirjutage kuut: "))
aasta=int(input("kirjutage aasta: "))

print(date(paev, kuu, aasta))

#(6)
arv=int(input("Sisestage arvu: "))
print(is_prime(arv))


#(4)
while True:
    try:
        kuu=int(input("Kuu number: "))
        break
    except:
        print("viga")
a=season(kuu)
print(a)







#(3)
while True:
    try:
        a=float(input("Sisesta külg: "))
        break
    except:
        print("viga")
S,P,d=square(a)
print(f"S={S}, P={P}, d={d}")









#(2)

while True:
    try:
        aasta=int(input("Sisesta aasta number: "))
        break
    except:
        print("viga")
a=liigaasta(aasta)
print(a)








#(1)
#b=int(input("Sisesta arv2: "))
#summa_3=Summa(3,b,int(input("Kolmas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)

