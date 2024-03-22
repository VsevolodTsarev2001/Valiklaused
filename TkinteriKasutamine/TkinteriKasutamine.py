from tkinter import *
k=0
def vajuta():
    global k
    k+=1
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k)
def tst_psse(event):
    t=textbox.get()
    pealkiri.configure(text=t,width=len(t))
    textbox.delete(0,END)
def valik():
    arv=var.get()
    textbox.delete(0,END)
    textbox.insert(END,arv)
aken=Tk()
aken.geometry("500x500")
aken.iconbitmap('icon.ico')
aken.title("Tkinteri kasutamine")
tekst="Pealkiri"
pealkiri=Label(aken,
              text=tekst,
              bg="#00c8ff",
              fg="#000080",
              font="Algerian 20",
              height=3, width=len(tekst),
              cursor="man")
textbox=Entry(aken,
              bg="#000080",
              fg="#00c8ff",
              font="Algerian 20", 
              width=20, 
              justify=CENTER) #show="*"
nupp=Button(aken, 
            text="Vajuta mind!", 
            font="Arial 20", 
            height=3, width=len(tekst), 
            relief=RAISED, 
            bg="#003366",
            command=vajuta) #SUNKEN, GROOVE, RAISED
f=Frame(aken)
var=IntVar() #StringVar()
e=Radiobutton(f,text="Esimene",variable=var,value=1,font="Arial 20",bg="#caff70",command=valik)
t=Radiobutton(f,text="Teine",variable=var,value=2,font="Arial 20",bg="#caff70",command=valik)
k_=Radiobutton(f,text="Kolmas",variable=var,value=3,font="Arial 20",bg="#caff70",command=valik)
nupp.bind("<Button-3>",vajuta_) #PKM
textbox.bind("<Return>",tst_psse) #Enter

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()
obj2=[e,t,k_]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=i)
aken.mainloop()
