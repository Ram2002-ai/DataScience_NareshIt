import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# 🔹 CONFIG (CHANGE SERVER NAME ONLY)
SERVER_NAME = "DESKTOP-H21E7ET"   # 🔥 CHANGE THIS

# 🔹 STEP 1: CREATE DATABASE IF NOT EXISTS
def create_database():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER_NAME};"
        "Trusted_Connection=yes;"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("IF DB_ID('webgui') IS NULL CREATE DATABASE webgui")

    conn.close()

# 🔹 STEP 2: CONNECT TO DATABASE
def get_db_connection():
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER_NAME};"
        "DATABASE=webgui;"
        "Trusted_Connection=yes;"
    )

# 🔹 STEP 3: CREATE TABLE IF NOT EXISTS
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    IF OBJECT_ID('registration', 'U') IS NULL
    CREATE TABLE registration (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name VARCHAR(100),
        course VARCHAR(100),
        fee INT
    )
    """)

    conn.commit()
    conn.close()

# 🔹 ADD STUDENT
def add_student():
    studentname = e2.get()
    coursename = e3.get()
    fee = e4.get()

    if not studentname or not coursename or not fee:
        messagebox.showerror("Error", "All fields required")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO registration (name, course, fee) VALUES (?, ?, ?)",
        (studentname, coursename, fee)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Record Added")
    clear_fields()
    load_students()

# 🔹 UPDATE
def update_student():
    studentid = e1.get()
    if not studentid:
        messagebox.showerror("Error", "Select record")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE registration SET name=?, course=?, fee=? WHERE id=?",
        (e2.get(), e3.get(), e4.get(), studentid)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Record Updated")
    clear_fields()
    load_students()

# 🔹 DELETE
def delete_student():
    studentid = e1.get()
    if not studentid:
        messagebox.showerror("Error", "Select record")
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM registration WHERE id=?", (studentid,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Record Deleted")
    clear_fields()
    load_students()

# 🔹 LOAD DATA
def load_students():
    for row in listBox.get_children():
        listBox.delete(row)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registration")
    for row in cursor.fetchall():
        listBox.insert("", "end", values=row)

    conn.close()

# 🔹 SELECT EVENT
def on_select(event):
    selected = listBox.selection()
    if selected:
        values = listBox.item(selected)['values']

        e1.config(state="normal")
        e1.delete(0, tk.END)
        e1.insert(0, values[0])

        e2.delete(0, tk.END)
        e2.insert(0, values[1])

        e3.delete(0, tk.END)
        e3.insert(0, values[2])

        e4.delete(0, tk.END)
        e4.insert(0, values[3])

# 🔹 CLEAR
def clear_fields():
    e1.config(state="normal")
    e1.delete(0, tk.END)
    e1.config(state="disabled")

    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)

# 🔹 INITIAL SETUP
create_database()
create_table()

# 🔹 UI
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

tk.Label(root, text="ID").grid(row=0, column=0)
tk.Label(root, text="Name").grid(row=1, column=0)
tk.Label(root, text="Course").grid(row=2, column=0)
tk.Label(root, text="Fee").grid(row=3, column=0)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)
e1.config(state="disabled")

e2 = tk.Entry(root)
e2.grid(row=1, column=1)

e3 = tk.Entry(root)
e3.grid(row=2, column=1)

e4 = tk.Entry(root)
e4.grid(row=3, column=1)

tk.Button(root, text="Add", command=add_student).grid(row=4, column=0)
tk.Button(root, text="Update", command=update_student).grid(row=4, column=1)
tk.Button(root, text="Delete", command=delete_student).grid(row=4, column=2)

cols = ("id", "name", "course", "fee")
listBox = ttk.Treeview(root, columns=cols, show="headings")
listBox.grid(row=5, column=0, columnspan=3)

for col in cols:
    listBox.heading(col, text=col)

listBox.bind("<ButtonRelease-1>", on_select)

load_students()

root.mainloop()