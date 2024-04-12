from ctypes import c_bool, c_buffer, c_byte, c_char
from decimal import ROUND_05UP
from operator import truediv
from pickletools import read_bytes1
from tkinter import *
from tkinter import messagebox as mb
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def figure():
    global var 
    valik=var.get()
    if valik==1:
        kala()
    elif valik==2:
        Vihmavari()
    elif valik==3:
        koon()
    elif valik==4:
        Prillid()
    elif valik==5:
        liblikas()


def calculate_equation():
    a_ = float(textbox.get())
    b_ = float(textbox2.get())
    c_ = float(textbox3.get())
    D = b_**2 - 4*a_*c_  # Discriminant
    if D > 0:
        x1_ = round((-1*b_ + sqrt(D)) / (2*a_), 2)
        x2_ = round((-1*b_ - sqrt(D)) / (2*a_), 2)
        t = f"X1={x1_}, X2={x2_}"
        discriminant_label.config(text=f"D = {D}, {t}")
        graf = True 
    elif D == 0:
        x1_ = round((-1*b_ + sqrt(D)) / (2*a_), 2)
        t = f"X1={x1_}"
        discriminant_label.config(text=f"D = {D}, {t}")
        graf = True
    else:
        t = "Корней нет"
        discriminant_label.config(text=f"D = {D}, {t}")
        graf = False
    mb.showinfo("Результат", t)

def graafik():
    a_ = float(textbox.get())
    b_ = float(textbox2.get())
    c_ = float(textbox3.get())
    D = b_**2 - 4*a_*c_  # Discriminant
    if D >= 0:
        x0 = (-b_) / (2*a_)
        y0 = a_*x0**2 + b_*x0 + c_ 
        x1 = np.arange(x0 - 10, x0 + 10, 0.5)
        y1 = a_*x1**2 + b_*x1 + c_
        fig = plt.figure()
        plt.plot(x1, y1, 'r-*')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text = f"Вершина параболы ({x0},{y0})"
    else:
        text = "Невозможно построить график"
    vastus.configure(text=f"D={D}\n{text}")

def kala():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2**2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5, 8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-12.5,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def Vihmavari():
    x1=np.arange(-12,12.5,0.5)
    y1=-(1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=-(1/8)*x2**2+6
    x3=np.arange(-12,-3.5,0.5)
    y3=-(1/8)*(x3+8)**2+6
    x4=np.arange(4,12.5,0.5)
    y4=-(1/8)*(x4-8)**2+6
    x5=np.arange(-4,0,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,1,0.5)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def koon():
    x1=np.arange(-7,7.5,0.5)
    y1=(3/49)*x1**2+8
    x2=np.arange(-7,7.5,0.5)
    y2=(4/49)*x2**2+1
    x3=np.arange(-6.8,-1.5,0.5)
    y3=-0.75*(x3+4)**2+11
    x4=np.arange(2,7,0.5)
    y4=-0.75*(x4-4)**2+11
    x5=np.arange(-5.8,-2.5,0.5)
    y5=-(x5+4)**2+9
    x6=np.arange(2.8,6,0.5)
    y6=-(x6-4)**2+9
    x7=np.arange(-4,4.5,0.5)
    y7=(4/9)*x7**2-5
    x8=np.arange(-5.2,5.5,0.5)
    y8=(4/9)*x8**2-9
    x9=np.arange(-7,-2.5,0.5)
    y9=(1/16)*(x9+3)**2-6
    x10=np.arange(2.8,7.5,0.5)
    y10=-(1/16)*(x10-3)**2-6
    x11=np.arange(-7,0.5,0.5)
    y11=(1/9)*(x11+4)**2-11
    x12=np.arange(0,7.5,0.5)
    y12=(1/9)*(x12-4)**2-11
    x13=np.arange(-7,-4,0.5)
    y13=-(x13+5)**2
    x14=np.arange(4.5,7.5,0.5)
    y14=-(x14-5)**2
    x15=np.arange(-3,3.5,0.5)
    y15=(2/9)*x15**2+2
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15)
    plt.title("Koon")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def Prillid():
    x1=np.arange(-9,-0.5,0.5)
    y1=-(1/16)*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=-(1/16)*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=(1/4)*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=-(1/4)*(x3-5)**2-3
    x5=np.arange(-9,-5.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-0.5*x7**2+1.5
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("Prillid")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def liblikas():
    x1=np.arange(-9,-0.5,0.5)
    y1=-(1/8)*(x1+9)**2+8
    x2=np.arange(1,9.5,0.5)
    y2=-(1/8)*(x2-9)**2+8
    x3=np.arange(-9,-7.5,0.5)
    y3=7*(x3+8)**2+1
    x4=np.arange(8,9.5,0.5)
    y4=7*(x4-8)**2+1
    x5=np.arange(-8,-0.5,0.5)
    y5=(1/49)*(x5+1)**2
    x6=np.arange(1,8.5,0.5)
    y6=(1/49)*(x5-1)**2
    x7=np.arange(-8,-0.5,0.5)
    y7=-(4/49)*(x7+1)**2
    x8=np.arange(1,8.5,0.5)
    y8=-(4/49)*(x7-1)**2
    x9=np.arange(-8,-1.5,0.5)
    y9=(1/3)*(x9+5)**2-7
    x10=np.arange(2,8.5,0.5)
    y10=-(1/3)*(x10-5)**2-7
    x11=np.arange(-2,-0.5,0.5)
    y11=-2*(x11+1)**2-2
    x12=np.arange(1,2.5,0.5)
    y12=-2*(x12-1)**2-2
    x13=np.arange(-1,1.5,0.5)
    y13=-4*x13**2+2
    x14=np.arange(-1,1.5,0.5)
    y14=4*x14**2-6
    x15=np.arange(-2,0.5,0.5)
    y15=-1.5*x15+2
    x16=np.arange(0,2.5,0.5)
    y16=1.5*x16+2
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,x12,y12,x13,y13,x14,y14,x15,y15,x16,y16)
    plt.title("Liblikas")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()
aken = Tk()
aken.geometry("1100x400")
aken.iconbitmap('book.ico')
aken.title("Квадратные уравнения")

tekst = "Решение квадратного уравнения"
pealkiri = Label(aken, text=tekst, bg="#6299a5", fg="#0f682e", font="Calibri 20", width=len(tekst), cursor="man")
textbox = Entry(aken, bg="#6299a5", fg="#0f682e", font="Algerian 20", width=4, justify=CENTER)
textbox2 = Entry(aken, bg="#6299a5", fg="#0f682e", font="Algerian 20", width=4, justify=CENTER)
textbox3 = Entry(aken, bg="#6299a5", fg="#0f682e", font="Algerian 20", width=4, justify=CENTER)


var = IntVar()

r1=Radiobutton(aken,text="kala",variable=var,value=1,font="Arial 20",bg="#caff70",command=figure)
r2=Radiobutton(aken,text="Vihmavari",variable=var,value=2,font="Arial 20",bg="#caff70",command=figure)
r3=Radiobutton(aken,text="koon",variable=var,value=3,font="Arial 20",bg="#caff70",command=figure)
r4=Radiobutton(aken,text="Prillid",variable=var,value=4,font="Arial 20",bg="#caff70",command=figure)
r5=Radiobutton(aken,text="liblikas",variable=var,value=5,font="Arial 20",bg="#caff70",command=figure)

label1=Label (aken, text="x**2+", fg="#0f682e", font="Calibri 20", width=5)
label2=Label (aken, text="x+", fg="#0f682e", font="Calibri 20", width=2)
label3=Label (aken, text="=0", fg="#0f682e", font="Calibri 20", width=2)

nupp = Button(aken, text="Решить", font="Arial 20", height=1, width=6, relief=RAISED, bg="#065535", fg="#1d1d1d", command=calculate_equation)
graafik_button = Button(aken, text="График", font="Arial 20", height=1, width=6, relief=RAISED, bg="#065535", fg="#1d1d1d", command=graafik)
discriminant_label = Label(aken, text="", bg="#6299a5", fg="#0f682e", font="Calibri 20", width=20, justify=LEFT)
vastus = Label(aken, text="", bg="#6299a5", fg="#0f682e", font="Calibri 20", width=20, justify=CENTER)

pealkiri.grid(row=0,column=1,columnspan=7)
textbox.grid(row=1,column=0)
label1.grid(row=1,column=1)
textbox2.grid(row=1,column=2)
label2.grid(row=1,column=3)
textbox3.grid(row=1,column=4)
label3.grid(row=1,column=5)
nupp.grid(row=1,column=6)
graafik_button.grid(row=1,column=7)
discriminant_label.grid(row=2,column=1,columnspan=6)
r1.grid(row=3,column=1)
r2.grid(row=4,column=1)
r3.grid(row=5,column=1)
r4.grid(row=6,column=1)
r5.grid(row=7,column=1)
aken.mainloop()