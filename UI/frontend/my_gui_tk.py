import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")


def say_hello():
    print("Hello, Tkinter!")

button = ttk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

root.mainloop()