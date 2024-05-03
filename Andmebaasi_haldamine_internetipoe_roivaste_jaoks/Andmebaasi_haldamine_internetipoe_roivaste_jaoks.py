import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from sqlite3 import *
from sqlite3 import Error
from os import path

# Andmebaasiühenduse loomine
def create_connection(db_file):
    print(f"Kasutatakse andmebaasi faili: {db_file}")  # Lisame väljundit
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

# Andmebaasiühenduse taasühendamine
def reconnect_to_database():
    global conn
    dbdir = path.dirname(__file__)
    dbpath = path.join(dbdir, "data.db")
    conn = create_connection(dbpath)

# Andmebaasist toodete kuvamine
def display_products():
    try:
        tree.delete(*tree.get_children())
        select_products = """
        SELECT Tooted.toote_nimi, Tooted.hind, Kategooriad.kategooria_nimi, Brändid.brändi_nimi
        FROM Tooted
        JOIN Kategooriad ON Tooted.kategooria_id = Kategooriad.kategooria_id
        JOIN Brändid ON Tooted.brändi_id = Brändid.brändi_id;
        """
        for row in execute_read_query(conn, select_products):
            tree.insert("", "end", values=row)
    except Exception as e:
        print(f"Viga toodete kuvamisel: {e}")
        reconnect_to_database()
        

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
    display_products()  # Kuvab uue toote koos olemasolevate toodetega

# Toote broneerimine
def book_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Teade", "Palun valige toode broneerimiseks!")
        return

    toote_nimi = tree.item(selected_item, 'values')[0]
    kuupäev = simpledialog.askstring("Broneering", f"Palun sisestage broneerimise kuupäev tootele '{toote_nimi}':")

    if not kuupäev:
        return  # Tühja kuupäeva korral ei tee midagi

    try:
        insert_booking = f"""
        INSERT INTO Broneeringud (toote_nimi, broneerimise_kuupäev)
        VALUES ('{toote_nimi}', '{kuupäev}');
        """
        execute_query(conn, insert_booking)
        messagebox.showinfo("Teade", "Toode on broneeritud edukalt!")
    except Error as e:
        print(f"Viga toote broneerimisel: {e}")

# Andmebaasiühenduse loomine
dbdir = path.dirname(__file__)
dbpath = path.join(dbdir, "data.db")
conn = create_connection(dbpath)

# Tkinteri rakendus
root = tk.Tk()
root.title("Toodete Haldamine")
root.geometry("800x400")

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
combo_kategooria["values"] = ["Elektroonika", "Riided"]
combo_kategooria.current(0)

label_bränd = tk.Label(root, text="Bränd:")
label_bränd.grid(row=3, column=0, padx=5, pady=5)
combo_bränd = ttk.Combobox(root)
combo_bränd.grid(row=3, column=1, padx=5, pady=5)
combo_bränd["values"] = ["Sony", "Nike"]
combo_bränd.current(0)

btn_add_product = tk.Button(root, text="Lisa uus toode", command=add_product)
btn_add_product.grid(row=4, column=0, columnspan=2, pady=10)

# Nupp toote broneerimiseks
btn_book_product = tk.Button(root, text="Broneeri toode", command=book_product)
btn_book_product.grid(row=5, column=0, columnspan=2, pady=10)

# Toodete kuvamise tabel
tree = ttk.Treeview(root, columns=("Toote nimi", "Hind", "Kategooria", "Bränd"), show="headings")
tree.heading("Toote nimi", text="Toote nimi")
tree.heading("Hind", text="Hind")
tree.heading("Kategooria", text="Kategooria")
tree.heading("Bränd", text="Bränd")
tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Andmete kuvamine tabelisse
display_products()

root.mainloop()

# Andmebaasiühenduse sulgemine
conn.close()