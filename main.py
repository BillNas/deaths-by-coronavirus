import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd 

master = tk.Tk()

canvas1 = tk.Canvas(master, width = 800, height = 300)
canvas1.pack()

label1 = tk.Label(master, text='Deaths by Covid-19')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)

countryName = tk.Entry (master)
canvas1.create_window(400, 100, window=countryName) 

def search():
	df = pd.read_csv('total_deaths.csv')
	date = df['date']
	country = df[countryName.get().capitalize()]
	figure1 = Figure(figsize=(4,3), dpi=100) 
	subplot1 = figure1.add_subplot(111) 
	xAxis = date
	yAxis = country
	subplot1.plot(xAxis,yAxis, color = 'orange',marker='8') 
	bar1 = FigureCanvasTkAgg(figure1, master) 
	bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

button1 = tk.Button (master, text=' Search ',command=search, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 180, window=button1)
button2 = tk.Button (master, text=' Exit ',command=master.quit, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(400, 220, window=button2)

mainloop()
