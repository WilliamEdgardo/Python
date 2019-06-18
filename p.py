from Tkinter import *
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

raiz=Tk()
raiz.title("DFT UART")

raiz.resizable(0,0)

#raiz.iconbitmap("gato.ico")
raiz.geometry("180x115")
raiz.config(bd=10)

COM = StringVar()
g=1

def abrir():
	try:
		# Iniciando conexion serial
		#puertoS = serial.Serial(str(COM.get()), 57600)
		puertoS = serial.Serial('/dev/ttyACM0', 19200, timeout=0.00000000000001)
		puertoS.close()
		puertoS.open()
		graficar(puertoS)
	except: 
		print("Puerto no disponible ....")

def cerrar():
	try:
		print("Cerrando puerto .....")
		plt.close("all")
		#raiz.destroy()
	except: 
		print("Error....")
plt.ion()
x=range(64)
def graficar(puertoS):	
	B=0
	y=list()
	z=list()
	while True:
		plt.figure('DFT en tiempo real')
		mag = puertoS.readline()
		if mag == '\n':
			B=1	
		elif B==1:
			y.append(float(mag.decode())/100.0)
			#print(float(mag.decode())/100.0)
				
		if len(y) == 32:
			z.extend(y)
			z.append(0)
			y.pop(0)
			y.reverse()
			z.extend(y)
			plt.clf()
			plt.stem(x,z)
			B=0
			y=list()
			z=list()

		plt.show()	
		plt.pause(0.000000001)	
	
Label(raiz, text="Ingrese el puerto").pack()
Entry(raiz, justify="center", textvariable=COM).pack()

Button(raiz, text="Abrir puerto", command=abrir).pack()

Button(raiz, text="Cerrar puerto", command=cerrar).pack()

raiz.mainloop()

