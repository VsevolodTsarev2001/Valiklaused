palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

# 1. Добавить еще несколько человек и зарплат(кол-во говорит пользователь)
def lisa_inimesi_ja_palgad(i:list,p:list,n=1)->any:
    """Funktsioon tagastab loendid, kus lisatud inimesi ja palka

    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :param int n:Inimeste arv
    :rtype: list,list
    """
    if n>0:
        for j in range(n):
            nimi = input("Sisestage inimese nimi: ").capitalize()
            palk = int(input("Sisestage inimese palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p

def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])
# 2. Удалить человека и его зарплату(вводим имя)
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid järjendid
    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """
    nimi=input("Keda kustutada ära(nimi): ")
    for j in range(len(i)):
        if nimi in i:
            i.remove()
            p.pop(j)
    return i,p

# 3. Самую большую зарплату и кто ее получает
def kellel_on_suurim_palk(i:list,p:list)->any:
    """Funktsioon näitab kellel on suurim palk
    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

# 4. Кто получает самую маленькую зарплату и какую именно
def kellel_on_vaiksem_palk(i:list,p:list):
    """
    """
    nimed=[]
    min_palk=min(p)
    ind=p.index(min_palk)
    mitu=p.count(min_palk)
    for j in range(mitu):
        nimi=i[p.index(min_palk,ind)]
        nimed.append(nimi)
        ind=+1
    return nimed

# 5. Упорядочить зарплаты в порядке возрастания и убывания вместе с именами
def sorteeritud_palga_jarjekord(suund):
    if suund.lower() == "kasvav":
        sorted_pairs = sorted(zip(palgad, inimesed))
    elif suund.lower() == "kahanev":
        sorted_pairs = sorted(zip(palgad, inimesed), reverse=True)
    else:
        print("Vale suund!")
        return
    return sorted_pairs

#5.1
def sorteerimine(i:list,p:list):
    """Funktsioon sorteerib inimesed
    :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p
# 6. Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран
def sama_palk():
    duplikaadid = {}
    for i, palk in enumerate(palgad):
        if palk in duplikaadid:
            duplikaadid[palk].append(inimesed[i])
        else:
            duplikaadid[palk] = [inimesed[i]]
    for palk, inimesed in duplikaadid.items():
        if len(inimesed) > 1:
            print(f"{len(inimesed)} inimest saavad palka {palk}: {', '.join(inimesed)}")

#6.1 
def vordsed_palgad(i:list,p:list)->list:
    """
    """
    nimed=[]
    #for id_, palgad in enumerate(p):
    #    print(id_,palgad)
    for palk in p:
        n=p.count(palk) 
        if n>1:
            subnimed=[]
            for j in range(n):
                nimi=i[p.index(palk,ind)]
                subnimed.append(nimi)
                p.pop(ind)
                i.pop(ind)
                ind=+1
            nimed.append(subnimed)
    print(nimed) 


# 7. Сделать поиск зарплаты по имени человека. Учесть, что имена могут повторяться
def otsi_palk(nimi):
    indeksid = [i for i, x in enumerate(inimesed) if x == nimi]
    palgad_nimedega = [(palgad[i], inimesed[i]) for i in indeksid]
    return palgad_nimedega

#7.1
def palk_nimi_jargi(i:list,p:list)->dict:
    """Funktsioon palgaotsing isiku nime järgi
     :param list i:Inimeste järjend
    :param list p:Palgate järjend
    :rtype: list,list
    """


# 8. Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма
def filtreeri_palk(eraldi, summa):
    if eraldi.lower() == "rohkem":
        inimesed_palgaga = [(inimesed[i], palgad[i]) for i in range(len(palgad)) if palgad[i] > summa]
    elif eraldi.lower() == "vahem":
        inimesed_palgaga = [(inimesed[i], palgad[i]) for i in range(len(palgad)) if palgad[i] < summa]
    else:
        print("Vale valik!")
        return
    return inimesed_palgaga

# 9. Top() - Т самых бедных и самых богатых человека
def top_palgad(T):
    top_bogatich = sorted(zip(palgad, inimesed), reverse=True)[:T]
    top_bednich = sorted(zip(palgad, inimesed))[:T]
    return top_bogatich, top_bednich

# 10. Keskmine() - Среднюю зарплату и имя человека ее получающего
def keskmine_palk():
    keskmine = sum(palgad) / len(palgad)
    indeks = min(range(len(palgad)), key=lambda i: abs(palgad[i] - keskmine))
    inimene = inimesed[indeks]
    return keskmine, inimene

# 11. Tulumaks() - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога
def tulumaks(nimi, palk):
    tulumaks = 0.20  # Eeldame, et tulumaksumäär on 20%
    maksma_kordades = palk * (1 - tulumaks)
    return maksma_kordades

# 12. Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)
def sorteeritud_nimi_jarjekord(suund):
    if suund.lower() == "a-z":
        sorted_pairs = sorted(zip(inimesed, palgad))
    elif suund.lower() == "z-a":
        sorted_pairs = sorted(zip(inimesed, palgad), reverse=True)
    else:
        print("Vale suund!")
        return
    return sorted_pairs

# 13. Находить тех кто получает зарплату ниже средней и удалить их из списков
def eemalda_alla_keskmine():
    keskmine = sum(palgad) / len(palgad)
    all_keskmisest = [(inimesed[i], palgad[i]) for i in range(len(palgad)) if palgad[i] < keskmine]
    for nimi, palk in all_keskmisest:
        inimesed.remove(nimi)
        palgad.remove(palk)
    print("Alla keskmise palka saavad inimesed on eemaldatud.")

# 14. Отредактировать списки таким образом, чтоб в списке людей имена были написаны с большой буквы, о зарплаты в формате int
def redigeeri_andmed():
    inimesed[:] = [nimi.capitalize() for nimi in inimesed]
    palgad[:] = [int(palk) for palk in palgad]
    print("Andmed on redigeeritud vastavalt nõudele.")

# 15. Каждый год работникам фирмы поднимают зарплату на 5%, узнай какой будут зарплаты/зарплата у определенного работника через Т лет.
def tulevased_palga_muudatused(aastad, nimi):
    indeks = inimesed.index(nimi)
    palk = palgad[indeks]
    for i in range(aastad):
        palk *= 1.05  # tõsta palka 5% võrra
    return palk

# 16. "Переименовать" каждого третьего человека. Новые имена вводит пользователь.
def renoveeri_kolmandad(uued_nimed):
    for i in range(2, len(inimesed), 3):
        inimesed[i] = uued_nimed.pop(0)

# 17. Написать функцию для редактирования данных. Пользователь выбирает, что редактировать: имя или зарплату. Измененние данные сохраняются  в список.
def redigeeri_andmeid(valik, vana, uus):
    if valik.lower() == "nimi":
        if vana in inimesed:
            indeks = inimesed.index(vana)
            inimesed[indeks] = uus.capitalize()
            print("Nimi on edukalt muudetud.")
        else:
            print("Sellist nime ei leitud.")
    elif valik.lower() == "palk":
        if vana in palgad:
            indeks = palgad.index(vana)
            palgad[indeks] = int(uus)
            print("Palk on edukalt muudetud.")
        else:
            print("Sellist palka ei leitud.")
    else:
        print("Vale valik!")

# 18. Найти имена начинающиеся на введенную букву и их зарплаты. Отобразить данные в столбик (Имя-зарплата)
def nimega_algavad_tähega(täht):
    match_inimesed = [(inimesed[i], palgad[i]) for i in range(len(inimesed)) if inimesed[i].startswith(täht)]
    for nimi, palk in match_inimesed:
        print(f"{nimi}-{palk}")

