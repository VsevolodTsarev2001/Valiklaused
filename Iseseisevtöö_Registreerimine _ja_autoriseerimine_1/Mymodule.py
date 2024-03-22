from dataclasses import dataclass
from os import system
from stringprep import c22_specials
from gtts import *
from random import *
import string
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def kirjuta_pas_ja_log(fail:str,l=[], p=[]):
    """Kirjutab failist andmed,mis oli sisestatud formaadis ""login:password" igas reas eraldi
    :param str fail:
    :param list l:
    :param list p:
    """
    f=open(fail,'w',encoding="utf-8")
    for i in range(len(l)):
        f.write(l[i]+":"+p[i]+"\n")
    f.close()
def loe_pas_ja_log(fail:str)->any:
    """Loeb failist andmed, mis oli sisestatud formaadis "login:password" igas reas eraldi
    :param str fail:
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8")#try
    l=[]
    p=[]
    for line in f:
        n=line.find(":")# login:password - разделитель
        log.append(line[0:n].strip())
        pas.append(line[n+1:len(line)].strip())
    f.close()
    return log,pas

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
    """
    """
    kirjuta_pas_ja_log
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
    """
    """
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
    """Muudab vana parooli uueks parooliks
    """
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
    """Funktsion taastab parool teile emailise
    """
    nimi = input("Sisesta oma nimi:")
    if nimi in l:
        ind = l.index(nimi)
        forgotten_password = p[ind]  # Получаем забытый пароль
        # Отправляем пароль по электронной почте
        try:
            context = ssl.create_default_context()
            smtp_server = "smtp.gmail.com"
            port = 587
            sender_email = "seva.tsarev@gmail.com"  # Укажите вашу электронную почту
            receiver_email = input("Sisesta oma emaili aadress, et saada unustatud parool: ")
            password = input("Type your password and press enter: ")
            subject = "Unustatud parool"
            body = f"Teie unustatud parool on: {forgotten_password}"
            
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            msg = message.as_string()

            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg)
            print("Unustatud parool on saadetud teie e-posti aadressile.")
        except Exception as e:
            print("Midagi läks valesti:", e)
        finally:
            server.quit()
    else:
        print("Nimi ei ole nimekirjas!")
#zbgi aydr mtrp stqf 
