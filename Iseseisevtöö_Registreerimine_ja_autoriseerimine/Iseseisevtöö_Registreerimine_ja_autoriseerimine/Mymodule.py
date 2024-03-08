from random import *
import string


def Salasona(k: int):
    """Funktsion 
    """
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus


def Registreerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    v=int(input("1-Ese koostan parooli\n2-Arvuti genireerib\n"))
    if v==1:
        pass
    else:
        salasona=Salasona(5)
        l.append(nimi)
        p.append(salasona)

    return l,p


def Autoriseerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    salasona=input("Sisesta oma salasõna:")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere tulemast!")
        else:
            print("Vale salasõna!")
    else:
        print("Nimi ei ole nimekirjas!")


def muuda_parool(l: list, p: list):
    nimi = input("Sisesta oma nimi:")
    vana_parool = input("Sisesta oma vana parool:")
    if nimi in l:
        ind = l.index(nimi)
        if vana_parool == p[ind]:
            uus_parool = input("Sisesta uus parool:")
            p[ind] = uus_parool
            print("Parool edukalt muudetud!")
        else:
            print("Vale vana parool!")
    else:
        print("Nimi ei ole nimekirjas!")


def taasta_parool(l: list, p: list):
    nimi = input("Sisesta oma nimi:")
    if nimi in l:
        ind = l.index(nimi)
        uus_parool = Salasona(5)  # Uue salasõna genereerimine
        p[ind] = uus_parool
        print("Teie uus parool on:", uus_parool)
    else:
        print("Nimi ei ole nimekirjas!")
#zbgi aydr mtrp stqf 




