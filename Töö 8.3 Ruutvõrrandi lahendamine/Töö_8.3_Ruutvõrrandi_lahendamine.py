import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def solve_equation():
    try:
        # Retrieve coefficients from the input fields
        a = float(sisse1.get())
        b = float(sisse2.get())
        c = float(sisse3.get())

        # Calculate the discriminant
        D = b**2 - 4*a*c

        # Solve the equation based on the discriminant
        if D > 0:
            x1 = (-b + np.sqrt(D)) / (2*a)
            x2 = (-b - np.sqrt(D)) / (2*a)
            result_label.config(text=f"lahendus: D={D:.2f}, x1 = {x1:.2f}, x2 = {x2:.2f}")
            plot_graph(a, b, c, x1, x2)
        elif D == 0:
            x = -b / (2*a)
            result_label.config(text=f"lahendus: x = {x:.2f}")
            plot_graph(a, b, c, x)
        else:
            result_label.config(text="pole paris lahendust")
            plot_graph(a, b, c)

    except ValueError:
        result_label.config(text="kirjutage korrektselt")

def plot_graph(a, b, c, *roots):
    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(6, 4))

    # Define the function
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a*x_vals**2 + b*x_vals + c

    # Plot the function
    ax.plot(x_vals, y_vals, label=f"f(x) = {a}x² + {b}x + {c}", color="blue")

    # Highlight the roots if they exist
    if roots:
        for root in roots:
            ax.plot(root, 0, 'ro')  # Roots marked with red points

    # Label the axes and title
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Graph of f(x) = {a}x² + {b}x + {c}")
    ax.axhline(0, color="black",linewidth=1)
    ax.axvline(0, color="black",linewidth=1)
    ax.grid(True)
    ax.legend()

    # Display the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=aken)  
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=200)  # Position the plot within the Tkinter window

# Tkinter setup
aken = Tk()
aken.title("Ruutvõrrandid")
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

sisse4 = Button(aken, text="lahenda", font=("Arial", 15), bg="darkgreen", fg="white", relief="raised", width=10, command=solve_equation)
sisse4.place(x=500, y=90)

result_label = Label(aken, text="= ?", font=("Arial", 15), bg="lightgrey", fg="green")
result_label.place(x=350, y=150)

aken.mainloop()
