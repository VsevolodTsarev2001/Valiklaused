from Mymodule import *
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]




while True:
    print("0-Naita andmed veerudes\n1-andemete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n4-Kellel on vaiksem palk\n5-Lalle\n6-vordsed_palgad\n7-palk nimi jargi\n")
    valik=int(input())
    if valik==1:
        inimesed,palgad=lisa_inimesi_ja_palgad(inimesed,palgad,int(input("Mitu inimest lisame? ")))
    elif valik==0:
        andmed_veerudes(inimesed, palgad)
    elif valik==2:
        andmete_eemaldamine_nimi_jargi(inimesed, palgad)
    elif valik==3:
        kellel_on_suurim_palk(inimesed, palgad)
    elif valik==4:
        kellel_on_vaiksem_palk(inimesed, palgad)
    elif valik==5:
        sorteerimine(inimesed, palgad)
    elif valik==6:
        vordsed_palgad(inimesed, palgad)
    elif valik==7:
        palk_nimi_jargi(inimesed, palgad)