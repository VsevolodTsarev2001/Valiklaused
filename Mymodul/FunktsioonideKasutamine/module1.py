from dataclasses import dataclass
from math import *
def Summa(arv1:int,arv2:int,arv3=0)->int:
    """ Funktsioon tagastab kolme arvu summa
        Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3 
    return s
def IntKontroll() -> any:
    """ Funktsioon tagastab sissestatud andme õiges formaadis
        IntKontroll()
    :rtype: any
    """
    x = input("Sisestage andme: ")
    try:
        x = int(x)
        return "int"
    except:
        try:
            x = float(x)
            return "float"
        except:
            return "str"

def arithmetic(x: int, y: int, op:str) -> float:
    """ Funktsioon tagastab kolme arvu summa
        arithmetic(x, y, op)
    :param int x: x sisestab kasutaja
    :param int y: y sisestab kasutaja
    :param str op: str sisestab kasutaja
    :rtype: int
    """
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if x == 0 or y == 0:
            print("jagamine nulliga ei ole võimalik")

def is_year_leap (aasta: int)->bool:
    """Funktsioon otsustab kas aasta on liigaasta või ei ole.
    Tagastad True kui aasta on liigaasta ja False kui aasta on tavaline aasta.

    :param int aasta: Aasta sisestab kasutaja 
    :rtype: bool
    """
    if aasta%4==0 and aasta%100!=0:
        return True
    else:
        return False


def square(külg:float)->any:
    """Funktsioon tagastab S,P,d



    :rtype:any
    """
    P=4*külg 
    S=külg**2
    d=külg*sqrt(2)
    return S,P,d 


def season (a:int)->str: 
    """
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12!\n Sisesta veel kord number: "))
            except:
                print("Viga andmetüübiga")
    if a==12 or a==1 or a==2:
        s="talv"
    elif a>2 and a<6:
        s="kevad"
    elif a in range(6,9,1):
        s="suvi"
    elif 9<=a<=11:
        s="sügis"
    return s