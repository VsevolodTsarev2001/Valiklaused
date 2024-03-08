from dataclasses import dataclass
from os import system
from stringprep import c22_specials
from gtts import *
def WB(a:int,c:int)->int:
    b=a*c 
    d=b//2
    return b,d 
print(WB)
 
def loe_failist(fail:str)->list:
    """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8")#try
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend
def kirjuta_failisse(fail:str,järjend=[]):
    """Ümber salvestame järdjendi failisse
    """
    n=int(input("Sisesta mitu elemendi: "))
    for i in range(n):
        järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,'w',encoding="utf-8")
    for element in järjend:
        f.write(element+'\n')
    f.close()
def heli(tekst:str, keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisesta tekst: ")
heli(tekst,'ru')

kirjuta_failisse("Text.txt")
paevad=loe_failist("Paevad.txt")
print(paevad)
