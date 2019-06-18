# Procesamiento Digital de Senales
# Proyecto: Reconocimiento de notas de Piano
# Hernandez Guzman William Edgardo --  Peralta Sanchez Fernado
# hdezgwilliam-gmail.com  --  fer_peralta10-hotmail.com

from Tkinter import *
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

raiz=Tk()
raiz.geometry("400x220")
raiz.title("Piano-UART")
raiz.configure(bg= "dark blue")
raiz.resizable(0,0)
image=PhotoImage(file="musical.png")
image=image.subsample(1,1)
fondo=Label(raiz, image=image).place(x=0,y=0,relwidth=1.0,relheight=1.0)

COM = StringVar()

FS = 13800

def abrir():
	try:
		# Iniciando conexion serial
		#puertoS = serial.Serial(str(COM.get()), 19200, timeout=1.0)
		puertoS = serial.Serial('/dev/ttyACM0', 19200, timeout=1.0)
		puertoS.close()
		puertoS.open()
		Cad.set("Abriendo puerto..")
		raiz.update_idletasks()
		time.sleep(1)
		frecuencia(puertoS)
	except: 
		print("Puerto no disponible ....")

def cerrar():
	try:
		print("Cerrando puerto .....")
		Cad.set("Cerrando ..")
		#L.grid().config()
		raiz.update_idletasks()
		time.sleep(1)
		raiz.destroy()
	except: 
		print("Error....")

def frecuencia(puertoS):	
	B=0
	f=0
	C="Iniciando ..."
	imprime(C)
	time.sleep(1)
	while True:	
		mag = puertoS.readline()
	
		if B==1:
			indice = float(mag.decode())
			f=indice*(FS/64)
			
			if f>4400.0 and f<4530.0:
				C="La nota es: RE1"
			elif f>4000 and f<4100:
				C="La nota es: DO1"
			elif f>3800 and f<3950:
				C="La nota es: SI"
			elif f>3400 and f<3500:
				C="La nota es: LA"
			elif f>3150 and f<3300:
				C="La nota es: SOL"
			elif f>2700 and f<2850:
				C="La nota es: FA"
			elif f>2450 and f<2600:
				C="La nota es: MI"
			elif f>2300 and f< 2400:
				C="La nota es: Re"
			elif f>2050 and f<2250:
				C="La nota es: DO"
			else :
				C = "Nota no reconocida"
			B=0
			imprime(C)
		if mag == '\n':
			B=1	

def imprime(C):
	if Cad.get()!=C:
		Cad.set(C)
		raiz.update_idletasks()
		#L.grid()
		time.sleep(0.08)
		#L.config(textvariable=Cad)


Cad = StringVar()
Cad.set("** Bienvenido **")
L = Label(raiz,textvariable=Cad,bg="lawn green",fg="white", font=("Agency FB",11)).place(x=135,y=180)

Label(raiz, text="Ingrese el puerto: ",bg="light sky blue",fg="black", height=1).place(x=25,y=10) #.pack(padx=4,pady=4,ipadx=5,ipady=5, fill=X)

Entry(raiz, justify="center", textvariable=COM, bg="light cyan",fg="black").place(x=145,y=10) #.pack(padx=3,pady=3,ipadx=3,ipady=3, fill=Y)

Button(raiz, text="Abrir puerto", command=abrir, bg="light salmon",fg="white").place(x=150, y=40)#.pack()

Button(raiz, text="Cerrar puerto", command=cerrar, bg="plum",fg="white").place(x=265, y=40)#.pack()

raiz.mainloop()

