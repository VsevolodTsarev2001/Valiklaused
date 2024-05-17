import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from sqlite3 import *
from sqlite3 import Error
from os import path

# Andmebaasiühenduse loomine

def create_connection(db_file):
    connection = None
    try:
        connection = connect(db_file)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection

# Päringu käivitamine

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Päring õnnestus!")
    except Error as e:
        print(f"Tekkis viga: {e}")

# Andmebaasist päringu tulemuse lugemine

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")

# Uue toote lisamine

def add_product():
    toote_nimi = entry_toote_nimi.get()
    hind = float(entry_hind.get())
    kategooria_nimi = combo_kategooria.get()
    brändi_nimi = combo_bränd.get()

    insert_new_product = f"""
    INSERT INTO Tooted (toote_nimi, hind, kategooria_id, brändi_id) 
    SELECT '{toote_nimi}', {hind}, Kategooriad.kategooria_id, Brändid.brändi_id
    FROM Kategooriad, Brändid
    WHERE Kategooriad.kategooria_nimi = '{kategooria_nimi}' AND Brändid.brändi_nimi = '{brändi_nimi}';
    """
    execute_query(conn, insert_new_product)
    display_products()

# Andmebaasist toodete kuvamine

def display_products():
    tree.delete(*tree.get_children())
    select_products = """
    SELECT Tooted.toote_nimi, Tooted.hind, Kategooriad.kategooria_nimi, Brändid.brändi_nimi
    FROM Tooted
    JOIN Kategooriad ON Tooted.kategooria_id = Kategooriad.kategooria_id
    JOIN Brändid ON Tooted.brändi_id = Brändid.brändi_id;
    """
    for row in execute_read_query(conn, select_products):
        tree.insert("", "end", values=row)

# Uue toote eemaldamine

def delete_product():
    toote_nimi = entry_toote_nimi_delete.get()

    try:
        delete_product_query = f"""
        DELETE FROM Tooted
        WHERE toote_nimi = '{toote_nimi}'
        """
        execute_query(conn, delete_product_query)
        display_products()
    except Error as e:
        print(f"Viga toote kustutamisel: {e}")

# Удаление товаров по категории

def delete_products_by_category(category_name):
    try:
        delete_products_query = f"""
        DELETE FROM Tooted
        WHERE kategooria_id IN (
            SELECT kategooria_id FROM Kategooriad WHERE kategooria_nimi = '{category_name}'
        )
        """
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM Tooted WHERE kategooria_id IN (SELECT kategooria_id FROM Kategooriad WHERE kategooria_nimi = '{category_name}')")
        deleted_count = cursor.fetchone()[0]
        execute_query(conn, delete_products_query)
        display_products()
        messagebox.showinfo("Kustutamine", f"Kustutati {deleted_count} toodet kategooria '{category_name}' järgi.")
    except Error as e:
        print(f"Viga toodete kustutamisel: {e}")

# Удаление товаров по бренду

def delete_products_by_brand(brand_name):
    try:
        delete_products_query = f"""
        DELETE FROM Tooted
        WHERE brändi_id IN (
            SELECT brändi_id FROM Brändid WHERE brändi_nimi = '{brand_name}'
        )
        """
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM Tooted WHERE brändi_id IN (SELECT brändi_id FROM Brändid WHERE brändi_nimi = '{brand_name}')")
        deleted_count = cursor.fetchone()[0]
        execute_query(conn, delete_products_query)
        display_products()
        messagebox.showinfo("Kustutamine", f"Kustutati {deleted_count} toodet brändi '{brand_name}' järgi.")
    except Error as e:
        print(f"Viga toodete kustutamisel: {e}")

# Редактирование информации о товарах

def edit_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Viga", "Palun valige toode, mida soovite muuta.")
        return

    item_values = tree.item(selected_item)['values']
    if not item_values:
        messagebox.showerror("Viga", "Valitud toode ei sisalda väärtusi.")
        return

    toote_nimi = item_values[0]
    uus_hind = simpledialog.askfloat("Muuda hind", f"Palun sisestage uus hind tootele '{toote_nimi}':")
    if uus_hind is None:
        return  # Пользователь нажал "Отмена"

    try:
        update_query = f"""
        UPDATE Tooted
        SET hind = {uus_hind}
        WHERE toote_nimi = '{toote_nimi}';
        """
        execute_query(conn, update_query)
        messagebox.showinfo("Edukas", f"Toote '{toote_nimi}' hind on edukalt muudetud.")
        display_products()
    except Error as e:
        messagebox.showerror("Viga", f"Viga toote '{toote_nimi}' hinna muutmisel: {e}")

# Lisa uus kategooria

def add_category():
    kategooria_nimi = simpledialog.askstring("Lisa uus kategooria", "Palun sisestage uue kategooria nimi:")
    if kategooria_nimi:
        insert_category_query = f"""
        INSERT INTO Kategooriad (kategooria_nimi)
        VALUES ('{kategooria_nimi}');
        """
        try:
            execute_query(conn, insert_category_query)
            messagebox.showinfo("Edukas", f"Kategooria '{kategooria_nimi}' on lisatud.")
            update_category_combobox()
        except Error as e:
            messagebox.showerror("Viga", f"Viga kategooria '{kategooria_nimi}' lisamisel: {e}")

# Kustuta kategooria

def delete_category():
    kategooria_nimi = combo_kategooria.get()
    delete_category_query = f"""
    DELETE FROM Kategooriad
    WHERE kategooria_nimi = '{kategooria_nimi}';
    """
    try:
        execute_query(conn, delete_category_query)
        messagebox.showinfo("Edukas", f"Kategooria '{kategooria_nimi}' on kustutatud.")
        update_category_combobox()
    except Error as e:
        messagebox.showerror("Viga", f"Viga kategooria '{kategooria_nimi}' kustutamisel: {e}")

# Lisa uus bränd

def add_brand():
    brändi_nimi = simpledialog.askstring("Lisa uus bränd", "Palun sisestage uue brändi nimi:")
    if brändi_nimi:
        insert_brand_query = f"""
        INSERT INTO Brändid (brändi_nimi)
        VALUES ('{brändi_nimi}');
        """
        try:
            execute_query(conn, insert_brand_query)
            messagebox.showinfo("Edukas", f"Bränd '{brändi_nimi}' on lisatud.")
            update_brand_combobox()
        except Error as e:
            messagebox.showerror("Viga", f"Viga brändi '{brändi_nimi}' lisamisel: {e}")

# Kustuta bränd

def delete_brand():
    brändi_nimi = combo_bränd.get()
    delete_brand_query = f"""
    DELETE FROM Brändid
    WHERE brändi_nimi = '{brändi_nimi}';
    """
    try:
        execute_query(conn, delete_brand_query)
        messagebox.showinfo("Edukas", f"Bränd '{brändi_nimi}' on kustutatud.")
        update_brand_combobox()
    except Error as e:
        messagebox.showerror("Viga", f"Viga brändi '{brändi_nimi}' kustutamisel: {e}")

# Обновление списка категорий

def update_category_combobox():
    select_categories = "SELECT kategooria_nimi FROM Kategooriad;"
    categories = execute_read_query(conn, select_categories)
    combo_kategooria['values'] = [category[0] for category in categories]
    combo_kategooria.current(0)

# Обновление списка брендов

def update_brand_combobox():
    select_brands = "SELECT brändi_nimi FROM Brändid;"
    brands = execute_read_query(conn, select_brands)
    combo_bränd['values'] = [brand[0] for brand in brands]
    combo_bränd.current(0)

# Andmebaasiühenduse loomine

filename = path.abspath(__file__)
dbdir = path.dirname(filename)
dbpath = path.join(dbdir, "data.db")
conn = create_connection(dbpath)

# Tkinteri rakendus

root = tk.Tk()
root.title("Toodete Haldamine")
root.iconbitmap('finance.ico')
root.geometry("825x700")

# Sisestusväljad ja nupp uue toote lisamiseks

label_toote_nimi = tk.Label(root, text="Toote nimi:")
label_toote_nimi.grid(row=0, column=0, padx=5, pady=5)
entry_toote_nimi = tk.Entry(root)
entry_toote_nimi.grid(row=0, column=1, padx=5, pady=5)

label_hind = tk.Label(root, text="Hind:")
label_hind.grid(row=1, column=0, padx=5, pady=5)
entry_hind = tk.Entry(root)
entry_hind.grid(row=1, column=1, padx=5, pady=5)

label_kategooria = tk.Label(root, text="Kategooria:")
label_kategooria.grid(row=2, column=0, padx=5, pady=5)
combo_kategooria = ttk.Combobox(root)
combo_kategooria.grid(row=2, column=1, padx=5, pady=5)

label_bränd = tk.Label(root, text="Bränd:")
label_bränd.grid(row=3, column=0, padx=5, pady=5)
combo_bränd = ttk.Combobox(root)
combo_bränd.grid(row=3, column=1, padx=5, pady=5)

btn_add_product = tk.Button(root, text="Lisa uus toode", command=add_product)
btn_add_product.grid(row=4, column=0, columnspan=2, pady=10)

# Sisestusväljad ja nupp toote kustutamiseks

label_toote_nimi_delete = tk.Label(root, text="Kustutatava toote nimi:")
label_toote_nimi_delete.grid(row=5, column=0, padx=5, pady=5)
entry_toote_nimi_delete = tk.Entry(root)
entry_toote_nimi_delete.grid(row=5, column=1, padx=5, pady=5)

btn_delete_product = tk.Button(root, text="Kustuta toode", command=delete_product)
btn_delete_product.grid(row=6, column=0, columnspan=2, pady=10)

# Добавим кнопки для удаления по категории и бренду

btn_delete_by_category = tk.Button(root, text="Kustuta tooted kategooria järgi", command=lambda: delete_products_by_category(combo_kategooria.get()))
btn_delete_by_category.grid(row=7, column=0, columnspan=2, pady=10)

btn_delete_by_brand = tk.Button(root, text="Kustuta tooted brändi järgi", command=lambda: delete_products_by_brand(combo_bränd.get()))
btn_delete_by_brand.grid(row=8, column=0, columnspan=2, pady=10)

# Кнопка для редактирования товаров
btn_edit_product = tk.Button(root, text="Muuda toodet", command=edit_product)
btn_edit_product.grid(row=9, column=0, columnspan=2, pady=10)

# Кнопки для добавления и удаления категорий
btn_add_category = tk.Button(root, text="Lisa uus kategooria", command=add_category)
btn_add_category.grid(row=10, column=0, columnspan=2, pady=10)

btn_delete_category = tk.Button(root, text="Kustuta kategooria", command=delete_category)
btn_delete_category.grid(row=11, column=0, columnspan=2, pady=10)

# Кнопки для добавления и удаления брендов
btn_add_brand = tk.Button(root, text="Lisa uus bränd", command=add_brand)
btn_add_brand.grid(row=12, column=0, columnspan=2, pady=10)

btn_delete_brand = tk.Button(root, text="Kustuta bränd", command=delete_brand)
btn_delete_brand.grid(row=13, column=0, columnspan=2, pady=10)

# Toodete kuvamise таблица

tree = ttk.Treeview(root, columns=("Toote nimi", "Hind", "Kategooria", "Bränd"), show="headings")
tree.heading("Toote nimi", text="Toote nimi")
tree.heading("Hind", text="Hind")
tree.heading("Kategooria", text="Kategooria")
tree.heading("Bränd", text="Bränd")
tree.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

# Andmete kuvamine tabelisse

update_category_combobox()
update_brand_combobox()
display_products()
root.mainloop()

# Andmebaasiühenduse sulgemine

conn.close()

