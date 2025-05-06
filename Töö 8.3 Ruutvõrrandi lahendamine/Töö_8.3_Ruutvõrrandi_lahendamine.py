import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def lahenda_vorrand():
    try:
        a = float(sisse1.get())
        b = float(sisse2.get())
        c = float(sisse3.get())

        D = b**2 - 4*a*c

        if D > 0:
            x1 = (-b + np.sqrt(D)) / (2*a)
            x2 = (-b - np.sqrt(D)) / (2*a)
            tulemus_label.config(text=f"Lahendus: D={D:.2f}, x1 = {x1:.2f}, x2 = {x2:.2f}")
            joonista_graafik(a, b, c, x1, x2)
        elif D == 0:
            x = -b / (2*a)
            tulemus_label.config(text=f"Lahendus: x = {x:.2f}")
            joonista_graafik(a, b, c, x)
        else:
            tulemus_label.config(text="Pole reaalset lahendust")
            joonista_graafik(a, b, c)

    except ValueError:
        tulemus_label.config(text="Sisesta õiged väärtused")

def joonista_graafik():
    try:
        a = float(sisse1.get())
        b = float(sisse2.get())
        c = float(sisse3.get())

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='green')
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.title('Graafik: Ruutvõrrandi f(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        result_label.config(text="Sisesta õiged väärtused.")

aken = Tk()
aken.title("Ruutvõrrandi Lahendamine")
aken.geometry('700x600')
aken.configure(bg="grey")


pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", bg='lightgrey', font=('Arial', 16), fg='green')
pealkiri.place(x=220, y=20)

sisse1 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="black", width=4)
sisse1.place(x=200, y=100)

kiri1 = Label(aken, text="x² +", font=("Arial", 15), bg="lightgrey", fg="green")
kiri1.place(x=250, y=100)

sisse2 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="black", width=4)
sisse2.place(x=300, y=100)

kiri2 = Label(aken, text="x +", font=("Arial", 15), bg="lightgrey", fg="green")
kiri2.place(x=350, y=100)

sisse3 = Entry(aken, font=("Arial", 15), bg="lightblue", fg="black", width=4)
sisse3.place(x=400, y=100)

kiri3 = Label(aken, text="= 0", font=("Arial", 15), bg="lightgrey", fg="green")
kiri3.place(x=450, y=100)

sisse4 = Button(aken, text="Lahenda", font=("Arial", 15), bg="darkgreen", fg="white", relief="raised", width=10, command=lahenda_vorrand)
sisse4.place(x=500, y=90)

sisse5 = Button(aken, text="Graafik", font=("Arial", 15), bg="darkgreen", fg="white", relief="raised", width=10, command=joonista_graafik)
sisse5.place(x=500, y=140)

tulemus_label = Label(aken, text="= ?", font=("Arial", 15), bg="lightgrey", fg="green")
tulemus_label.place(x=300, y=150)





aken.mainloop()
