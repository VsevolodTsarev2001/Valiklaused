from re import A
from string import * 
from random import *
from time import sleep


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



##4
#Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    while True:
#        try:
#            indeks=int(input("Sisesta oma indeks: "))
#            indeks_elemendide_arv=len(str(indeks)) 
#            if indeks_elemendide_arv==5:
#                print("5numbriline indeks ")
#                break
#            else:
#                print("On vaja 5numbriline arv(indeks)")
#        except:
#            print("Vale andmetüüp!")
#    #arv1=indeks//10000
#    #print(arv1)
#    symbolid=list(str(indeks))
#    sym1=symbolid[0]
#    print(sym1)
#    print(f"Sa elad piirkonnas {Indeksid[int(symbolid[0])-1]}")

##5
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choise(ascii_uppercase))
#print(rida)
#kogus=int(input("Mitu elemendi vahetame oma vahel "))
#if len(rida)//2>=kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#print(rida)

##6
#numbers= input("Введите числа через пробел: ").split()
#numbers=list(map(int, numbers))
#if not numbers:
#    print("Ошибка: список чисел пуст.")
#else:
#    max_number=max(numbers)
#numbers[numbers.index(max_number)]=max

#9
while True:
    try:
        name = input("Sisestage nimi: ").strip()
        if not name.isalpha():
            raise ValueError("Nimi võib sisaldada ainult tähti.")
        break
    except ValueError as e:
        print(e)

print(f"Tere, {name.capitalize()}!")

vowels = 0
consonants = 0
for letter in name:
    if letter.lower() in 'aeiouõäöü':
        vowels += 1
    else:
        consonants += 1

print(f"Tähtede arv: {len(name)}")
print(f"Vokaalide arv: {vowels}")
print(f"Konsonantide arv: {consonants}")

unique_letters = sorted(set(name.lower()))
print("Tähestiku järjestuses nimi:", ", ".join(unique_letters))



#16
# Järjend vastustega
vastused = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]

print("Tere tulemast küsimuste ja vastuste programmi!")

while True:
    input("Küsige jah/ei küsimus: ")
    vastus = choice(vastused)
    print("Vastus:", vastus)
    if input("Kas soovite jätkata (jah/ei)? ").lower() != "jah":
        print("Aitäh ja head aega!")
        break



#18
print("Tere tulemast vene ruletti.!")
print("Revolveris on 6 padrunit, millest üks on tühi.")

while True:
    print("\nMe alustame uut mängu!")

    # Создаем список с патронами (1 - патрон, 0 - пусто)
    revolver = [0, 0, 0, 0, 0, 0]
    # Вставляем случайным образом один патрон
    revolver[randint(0, 5)] = 1

    input("Trummi keeramiseks vajutage Enter...")

    print("Trummi keerutamine...")
    sleep(2)  # Задержка для эффекта ожидания

    # Выбираем случайный патрон
    bullet_position = randint(0, 5)
    if revolver[bullet_position] == 1:
        print("lask!")
        print("Game over!")
    else:
        print("klick!")
        print("Sa jäid ellu!")

    play_again = input("Kas sa tahad uuesti mängida? (ja/ei): ").lower()
    if play_again != "ja":
        print("Aitäh mängimise eest! Kohtumiseni!")
        break