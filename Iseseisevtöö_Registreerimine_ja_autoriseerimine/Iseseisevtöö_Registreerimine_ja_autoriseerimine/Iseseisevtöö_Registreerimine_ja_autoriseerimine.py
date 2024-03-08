from Mymodule import *
p=[]
l=[]

while True:
    print(l)
    print(p)
    v=int(input("1-Registreerimine\n2-Aurotiseerimine\n3-Muuta_salasõna\n4-Taastamine\n5-Välja"))
    if v==1:
        l,p=Registreerimine(l,p)
        pass
    elif v==2:
        Autoriseerimine(l,p)
    elif v==3:
        muuda_parool(l,p)
    elif v==4:
        taasta_parool(l,p)
    elif v==5:
        break
    else:
        print("Tee õige valik")
