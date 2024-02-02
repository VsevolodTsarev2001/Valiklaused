#print("*** ARVUMÄNGUD ***")
#print()
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#while True:#все верно но для удобства использую while True
#    try:
#        a = abs(int(input("Sisesta täisarv => ")))#лишняя скобка
#        break
#    except ValueError:
#         print("See ei ole täisarv")
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#if a == 0:
#    print("Nulliga ei ole mõtet midagi teha")
#else:
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Määrame, mitu paaris- ja paaritut arvu antud arvus on")
#    print()
#    c = b = a  
#    paaris = 0
#    paaritu = 0
#    while b > 0:
#        if b % 2 == 0:
#            paaris =+ 1 
#        else:
#            paaritu =+ 1 
#        b = b // 10
    
#    print("Paarisarvud:", paaris)
#    print("Paaritud arvud:", paaritu)
#    print()
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#    print("*Pöörame ümber* sisestatud arvu")
#    print()
#    b = 0

#    while a > 0: # двоеточие в конце while
#        number = a % 10
#        a = a // 10
#        b = b * 10
#        b += number
#    print("*Ümberpööratud* arv on", b)
#    print()
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#    print("Kontrollime Collatzi hüpoteesi") # лишняя скобка
#    print()
#    if c % 2 == 0:
#        print("c on paarisarv. Jagame 2-ga.")
#    else:
#        print("c on paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
#    while c != 1:
#        if c % 2 == 0:
#            c //= 2
#        else:
#            c = (3 * c + 1) // 2
#        print(c, end=" ")
#    print()
#    print("Hüpotees kehtib")
a=2
b=2
b+=a
a=2*a+3*b
b=a/2*b
print(b)