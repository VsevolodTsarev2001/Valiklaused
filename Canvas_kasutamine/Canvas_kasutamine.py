
from tkinter import *
from tkinter import font
from random import choice
from math import *

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")
tahvel.pack()


item_var = StringVar()

def draw_estonia_flag():
    tahvel.delete("all")
    tahvel.create_rectangle(50, 50, 350, 100, fill="blue")
    tahvel.create_rectangle(50, 100, 350, 150, fill="black")
    tahvel.create_rectangle(50, 150, 350, 200, fill="white")

def draw_prantsusmaa_flag():
    tahvel.create_rectangle(0, 0, 300, 66, fill="#0C71C3")  # Верхняя полоса (синяя)
    tahvel.create_rectangle(0, 66, 300, 133, fill="#FED450")  # Средняя полоса (желтая)
    tahvel.create_rectangle(0, 133, 300, 200, fill="#0C71C3")  # Нижняя полоса (синяя)

def draw_bagami_flag():
   # Золотая полоса
    tahvel.create_rectangle(0, 67, 300, 133, fill="#FFD700")
    # Аквамариновая полоса слева
    tahvel.create_rectangle(0, 0, 300, 67, fill="#00778B")
    # Аквамариновая полоса справа
    tahvel.create_rectangle(0, 133, 300, 200, fill="#00778B")
    # Черный треугольник
    tahvel.create_polygon(0, 0, 150, 100, 0, 200, fill="black")

    # Синяя полоса слева
    tahvel.create_rectangle(0, 0, 100, 200, fill="#0055A4")
    # Белая полоса посередине
    tahvel.create_rectangle(100, 0, 200, 200, fill="#FFFFFF")
    # Красная полоса справа
    tahvel.create_rectangle(200, 0, 300, 200, fill="#EF4135")

def draw_chessboard():
    tahvel.delete("all")
    size = 600
    rows = cols = 8
    square_size = size // max(rows, cols)
    colors = ["white", "black"]    
    for row in range(rows):
        for col in range(cols):            
            color_index = (row + col) % 2  
            color = colors[color_index]            
            x0 = col * square_size
            y0 = row * square_size            
            x1 = x0 + square_size
            y1 = y0 + square_size            
            tahvel.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

def draw_rainbow_gradient():
    tahvel.delete("all")
    colors=["black", "cyan", "red", "blue", "gray", "yellow", "green", "lightblue", "pink", "gold"]
    x0 = y0 = 0
    x1 = y1 = 600
    p = 2
    for i in range(150):
        x0 += p 
        y0 += p 
        x1 -= p 
        y1 -= p
        tahvel.create_oval(x0, y0, x1, y1, fill=choice(colors))

def draw_infinite_shapes():
    tahvel.delete("all")
    x0 = y0 = 0
    x1 = y1 = 600
    p = 0
    x_ = y_ = 600
    for i in range(20):
        x0 += p 
        y0 += p 
        x1 -= p 
        y1 -= p 
        tahvel.create_rectangle(x0, y0, x1, y1 , fill="yellow")
        tahvel.create_oval(x0, y0, x1, y1, fill="magenta")
        x_ -= 2 * p 
        y_ -= 2 * p 
        p = int(((x_**2 + y_**2)**(1/2) - x_) / 2)
        p = int(((p**2) / 2)**(1/2))

def valgusfoor ():
        # Рисуем красный сигнал светофора
    red_light = tahvel.create_oval(50, 50, 150, 150, fill="gray")
    # Рисуем желтый сигнал светофора
    yellow_light = tahvel.create_oval(50, 180, 150, 280, fill="gray")
    # Рисуем зеленый сигнал светофора
    green_light = tahvel.create_oval(50, 310, 150, 410, fill="gray")
global red_light, yellow_light, green_light
    # Функция для изменения цвета светофора
def change_color():
    global red_light, yellow_light, green_light
    # Очищаем все сигналы светофора
    tahvel.itemconfig(red_light, fill="gray")
    tahvel.itemconfig(yellow_light, fill="gray")
    tahvel.itemconfig(green_light, fill="gray")
    # Определяем цвет сигнала в зависимости от текущего состояния
    current_color = next(light_colors)
    # Устанавливаем цвет текущему сигналу
    if current_color == "red":
        tahvel.itemconfig(red_light, fill="red")
    elif current_color == "yellow":
        tahvel.itemconfig(yellow_light, fill="yellow")
    elif current_color == "green":
        tahvel.itemconfig(green_light, fill="green")
    # Запускаем функцию снова через 2 секунды
    raam.after(2000, change_color)
    # Создаем бесконечный цикл изменения цвета светофора
light_colors = iter(["red", "yellow", "green"])
change_color()

def display_item():
    selected_item = item_var.get()
    if selected_item == "estonia":      
        draw_estonia_flag()
    elif selected_item == "prantsusmaa":    
        draw_prantsusmaa_flag()
    elif selected_item == "bahamas":        
        draw_bagami_flag()
    elif selected_item == "rainbow_ball":        
        draw_rainbow_gradient()
    elif selected_item == "square_in_square":        
        draw_infinite_shapes()
    elif selected_item == "chessboard":        
        draw_chessboard()
    elif selected_item == "valgusfoor":
        valgusfoor()

estonia_radio = Radiobutton(raam, text="Флаг Эстонии", variable=item_var, value="estonia", command=display_item)
estonia_radio.pack()

bahamas_radio = Radiobutton(raam, text="Флаг Багамских островов", variable=item_var, value="bahamas", command=display_item)
bahamas_radio.pack(pady=5)

russia_radio = Radiobutton(raam, text="Флаг Франции", variable=item_var, value="prantsusmaa", command=display_item)
russia_radio.pack(pady=5)

rainbow_radio = Radiobutton(raam, text="радужное_переливание", variable=item_var, value="rainbow_ball", command=display_item)
rainbow_radio.pack(pady=5)

square_radio = Radiobutton(raam, text="бесконечные квадратики и кружочки", variable=item_var, value="square_in_square", command=display_item)
square_radio.pack(pady=5)

chessboard_radio = Radiobutton(raam, text="Шахматы", variable=item_var, value="chessboard", command=display_item)
chessboard_radio.pack(pady=5)

valgusfoor_radio = Radiobutton(raam, text="Светофор", variable=item_var, value="valgusfoor", command=display_item)
valgusfoor_radio.pack(pady=5)

raam.mainloop()