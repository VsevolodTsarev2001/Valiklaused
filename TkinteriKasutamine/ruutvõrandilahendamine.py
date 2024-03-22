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
aken.geometry("700x250")
aken.iconbitmap('book.ico')
aken.title("Квадратные уравнения")
tekst="Решение квадратного уравнения"
pealkiri=Label(aken,
              text=tekst,
              bg="#6299a5",
              fg="#0f682e",
              font="Calibri 20",
              width=len(tekst),
              cursor="man")
textbox=Entry(aken,
              bg="#6299a5",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER)
k=Label(aken,
              bg="#000080",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER)
textbox2=Entry(aken,
              bg="#6299a5",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER) #show="*"
b=Label(aken,
              bg="#000080",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER) #show="*"
textbox3=Entry(aken,
              bg="#6299a5",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER) #show="*")
l=Label(aken,
              bg="#000080",
              fg="#0f682e",
              font="Algerian 20", 
              width=20, 
              justify=CENTER)
nupp=Button(aken, 
            text="Vajuta mind!", 
            font="Arial 20", 
            height=3, 
            width=len(tekst), 
            relief=RAISED, 
            bg="#065535",
            fg="#1d1d1d",
            command=vajuta) #SUNKEN, GROOVE, RAISED

obj=[pealkiri,textbox,k,textbox2,b,textbox3,l,nupp]
for i in obj:
    i.pack()
aken.mainloop()