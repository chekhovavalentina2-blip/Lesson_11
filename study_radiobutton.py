import tkinter as tk
from tkinter import messagebox


def study_radio():

    window = tk.Toplevel()
    window.title("Радиокнопки")
    window.geometry("300x200")

    var = tk.StringVar(value="python")

    tk.Label(window, text="Выберите язык").pack(pady=5)
    tk.Radiobutton(window, text="Python", variable=var, value="python").pack()
    tk.Radiobutton(window, text="Java", variable=var, value="java").pack()
    tk.Radiobutton(window, text="C++", variable=var, value="cpp").pack()


    def show_coice():
        messagebox.showinfo("Результат", f"Выбран: {var.get()}")


    tk.Button(window, text="Показать", command=show_coice).pack(pady=10)

