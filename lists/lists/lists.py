#from random import *
#nimed=["Mati","Meelis","Kati","Mati"]
#while True:
#    print("--------------------")
#    v=input("N-näita andmet\nL - lisa andmeid\nK-andmete kustutamine\nH-andmete haldus\nI-positsiooni otsing\n")
#    if v=="N":
#        v=input("Kas juhusik(j) nimi või terve loetelu(t)")
#        if v=="t":
#            print(nimed)
#        elif v=="j":
#            print(choice(nimed))
#    elif v=="L":
#        v=input("Kas nimekirja lõppu(l) või positsioonile(p)")
#        if v=="l":
#            nimi=input("Sisesta nimi:" )
#            nimed.append(nimi)
#        elif v=="p":
#            nimi=input("Sisesta nimi:" )
#            ind=int(input("Mis kohale:" ))
#            nimed.insert(ind-1,nimi)
#    elif v=="K":
#        v=input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed(k)")
#        if v=="i":
#            ind=int(input("Sisesta indeks:"))
#            nimed.pop(ind-1)
#        elif v=="k":
#            nimi.clear()
#        elif v=="n":
#            nimi=input("Sisesta nimi:  ")
#            mitu=nimed.count(nimi)
#            if mitu>0:
#                for i in range(mitu):
#                    nimed.remove(nimi)
#            elif v==nimi:
#                print(f"{nimi} ei ole loetelus")
#    elif v=="H":
#        v=input("Sorteerimine(s),kopeerimine(k) või ümber pööramine(p)")
#        if v=="s":
#            v=int(input("A-z(1) või Z-a?(2)"  ))
#            if v==1:
#                nimed.sort()
#            elif v==2:
#                nimed.sort(reverse=True)
#        elif v=="k":
#            nimed.copy()
#        elif v=="p":
#            nimed.reverse()
#    elif v.upper()=="I":
#        nimi=input("Sisesta nimi: ")
#        mitu=nimed.count(nimi)
#        if mitu>0:
#            print(f"Seal on {mitu} {nimi}")
#            for i in range(mitu):
#                print(f"{nimi} on {i+1} positsioonil")
#        else:
#            print(f"{nimi} ei ole loetelus.")


#2
#spc = "\n--------------------"
#nimed = ["Mati", "Meelis", "Kati", "Mati"]
#while True:
#    print("--------------------")
#    v = input("N-näita andmeid\nL-lisada andmeid\nK-andmete" + spc + "\n")
#    if v.upper() == "N":
#        v = input("Kas juhuslik(j) nimi või terve loetelu(t)? ")
#        if v.lower() == "t":
#            print(nimed)
#        elif v.lower() == "j":
#            print(choice(nimed))
#    elif v.upper() == "L":
#        v = input("Kas nimekirja lõppu(l) või positsioonile(p)? ")
#        if v.lower() == "l":
#            nimi = input("Sisesta nimi: ")
#            nimed.append(nimi)
#            print(spc, nimed, end=spc)
#        elif v.lower() == "p":
#            positsioonile = int(input("Sisesta positsioonile: "))
#            nimi = input("Sisesta nimi: ")
#            nimed.insert(positsioonile - 1, nimi)
#            print(spc, nimed, end=spc)
#    elif v.upper() == "K":
#        v = input("Kas nimi järgi(n), indeksi järgi(i) või kõik nimed(k)")
#        if v.lower() == "i":
#            ind = int(input("Sisesta indeks: "))
#            nimed.pop(ind-1)
#            print(spc, nimed, end=spc)
#        elif v.lower() == "n":
#            nimi = input("Sisesta nimi: ")
#            mitu = nimed.count(nimi)
#            if mitu > 0:
#                if mitu > 1:
#                    indeks = -1
#                    indeks_list = []
#                    for elem in nimed:
#                        ind += 1
#                        if elem == nimi:
#                            indeks_list.append(indeks)
#                    print(indeks_list)
#                    v = int(input("Mis indeks?"))
#                    nimed.pop(v)
#                else:
#                    nimed.remove(nimi)
#            else:
#                print(f"{nimi} ei ole loetelus")
#            print(spc, nimed, end=spc)
#        elif v.lower() == "k":
#            nimed.clear()
#            print(spc, nimed, end=spc)
