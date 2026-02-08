import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk

class Mandelbrot():
    #Zn+1 = Zn2 + C
    def __init__(self):
        self.threshold = 1

    def calculate(self, x, y, itr):
        c = complex(x, y)
        z = complex(0, 0)   

        for i in range(itr):
            z = z**2 + c
            if abs(z) > 4:
                return i
        return itr - 1
    
    def draw(self):
        ax.clear()

        x_start, y_start = -2, -1.5 
        width, height = 3, 3
        density = 100
        threshold = 50

        re = np.linspace(x_start, x_start + width, int(width * density))
        im = np.linspace(y_start, y_start + height, int(height * density))
        X = np.empty((len(re), len(im)))

        for i in range(len(re)):
            for j in range(len(im)):
                X[j, i] = self.calculate(re[i], im[j], self.threshold)
        
        ax.imshow(X, interpolation="bicubic", cmap='magma', extent=[x_start, x_start + width, y_start, y_start + height])
        ax.text(0.05, 0.95, f"Iterations: {self.threshold}", transform=ax.transAxes, color="white", fontsize=5, fontweight='bold',verticalalignment='top',bbox=dict(facecolor='black', alpha=0.5, edgecolor='none'))
        canvas.draw()

        if self.threshold < 10:
            self.threshold += 1
        else:
            self.threshold = int(self.threshold * 1.5)

root = tk.Tk()
root.title("Fractal Visualizer by quagdev")

fig, ax = plt.subplots(figsize=(3, 2.5))
mandelbrot = Mandelbrot()

label = tk.Label(font=("Courier", 24), text="Fractal Visualizer")
label.pack()    

canvas = FigureCanvasTkAgg(fig, master = root)
canvas.get_tk_widget().pack()

frame = tk.Frame(root)
frame.pack(pady=10)


tk.Button(frame, text="Mandelbrot", command=mandelbrot.draw, font=("Courier"), width = 10, height = 3).pack(side="left", padx=10)
tk.Button(frame, text="Quit", command=root.destroy, font=("Courier"), width = 10, height = 3).pack(side="right",padx=10)

root.mainloop()