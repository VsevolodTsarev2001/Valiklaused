from module1 import * #Summa as s
for i in range(5):
    [i] = 3
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
a=is_year_leap(aasta)
print(a)








#(1)
#b=int(input("Sisesta arv2: "))
#summa_3=Summa(3,b,int(input("Kolmas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)

