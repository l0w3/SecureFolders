from tkinter import ttk 
from tkinter import *
import os, sys
import webbrowser as wb
import time
import pickle



class SecureFolder:

	def __init__(self, window):
		
		#Creamos la ventana
		
		self.autenticado = False
		self.accion = root
		self.accion.iconbitmap("icono2.ico")
		self.accion.geometry("150x60")
		self.accion.title("SecureFolder")
		frame = LabelFrame(self.accion, text = "Autenticar")
		frame.grid(row = 0, column = 0, columnspan = 10, pady = 10)
		
		#En el caso de que este autenticado, le mostramos los botones de crear una carpeta, o abrirla
		
		if os.path.exists("Cookie") == True:
			if self.autenticado == True:

				ttk.Button(frame, text = "Crear una carpeta", command = self.crear).grid(row = 1, column = 1)
				ttk.Button(frame, text = "Abrir una carpeta", command = self.abrir).grid(row = 1, column = 3)
		
			#En el caso contrario, le mostramos la pantalla de autenticacion
			else:
				ttk.Button(frame, text = "Autenticar", command = self.password).grid(row = 1, column = 3, sticky = W + E)
		else:
			ttk.Button(frame, text = "Registrar", command = self.crearContraseña).grid(row = 1, column = 3, sticky = W + E)

	#Esta es la funcion de comprobacion, es igual que la anterior. Se ejecuta si no estabamos autenticados y nos autenticamos
	def comprobacion(self):
		self.accion.iconbitmap("icono2.ico")
		self.accion.geometry("250x60")
		frame = LabelFrame(self.accion, text = "Accion")
		frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
		
		if self.autenticado == True:
			ttk.Button(frame, text = "Crear una carpeta", command = self.crear).grid(row = 1, column = 1)
			ttk.Button(frame, text = "Abrir una carpeta", command = self.abrir).grid(row = 1, column = 3)
		else:
			ttk.Button(frame, text = "Autenticar", command = self.password).grid(row = 1, column = 3)
			

		
	# Esta funcion muestra el panel de login (Caja de texto con un boton) donde se introduce la contraseña y al pulsar el boton se redirecciona esta informacion a la funcion de autenticacion	
	def password(self):

		self.passwind = Toplevel()
		self.passwind.iconbitmap("icono2.ico")
		self.passwind.geometry("250x60")
		passframe = LabelFrame(self.passwind, text = "Autenticar")
		passframe.grid(row = 0, column = 0, columnspan = 3, pady = 10)
		self.passwd = Entry(passframe)
		self.passwd.focus()
		self.passwd.grid(row = 1, column = 1)
		ttk.Button(passframe, text = "Autenticar", command = self.autenticacion).grid(row = 1, column = 3)
	

	#Esta funcion es la de autenticacion, comprueba que la contraseña es correcta y si lo es, nos envia al panel de acciones
	def autenticacion(self):
		
		cookie = open("cookie", "rb")
		Contraseña = pickle.load(cookie)

		if self.passwd.get() == Contraseña:
			self.passwind.destroy()
			self.autenticado = True
			cookie.close()
			self.comprobacion()

	def crearContraseña(self):
		self.passCreate = Toplevel()
		self.passCreate.iconbitmap("icono2.ico")
		self.passCreate.geometry("250x60")
		createframe = LabelFrame(self.passCreate, text = "Registrar")
		createframe.grid(row = 0, column = 0, columnspan = 3, pady = 10)
		self.CreatePass = Entry(createframe)
		self.CreatePass.focus()
		self.CreatePass.grid(row = 1, column = 1)
		
		ttk.Button(createframe, text = "Registrar", command = self.registro).grid(row = 1, column = 3)
		

	def registro(self):
		cookie = open("cookie", "wb")
		pickle.dump(self.CreatePass.get(), cookie)
		cookie.close()
		self.autenticado = True
		self.comprobacion()
		try:
			self.passCreate.destroy()
			
		except AttributeError:
			pass

			 
			

			
	#Esta funcion abre un cuadro de dialogo donde introducimos los parametros de la carpeta a crear
	def crear(self):
		self.crear = Toplevel()
		self.crear.iconbitmap("icono2.ico")
		frame_crear = LabelFrame(self.crear)
		frame_crear.grid(row = 0, column = 0, columnspan = 3, pady = 20)

		Label(frame_crear, text = "Nombre de la carpeta: ").grid(row = 1, column = 0)
		self.nombre_carpeta = Entry(frame_crear)
		self.nombre_carpeta.focus()
		self.nombre_carpeta.grid(row = 1, column = 1)
		ttk.Button(frame_crear, text = "Crear carpeta", command = self.crear_carpeta).grid(row = 1, column = 3)

	#Esta funcion crea la carpeta con los parametros anteriores
	def crear_carpeta(self):
		
		os.makedirs(self.nombre_carpeta.get())
		os.system("REN " + self.nombre_carpeta.get() + " " + self.nombre_carpeta.get() + ".{2559a1f2-21d7-11d4-bdaf-00c04f60b9f0}")

		try:
			self.crear.destroy()
			
		except AttributeError:
			pass
		
			
		

	#En esta funcion introducimos los parametros de la carpeta que queremos abrir
	def abrir(self):
		self.abrir = Toplevel()
		self.abrir.iconbitmap("icono2.ico")
		frame_abrir = LabelFrame(self.abrir)
		frame_abrir.grid(row = 0, column = 0, columnspan = 3, pady = 20)

		Label(frame_abrir, text = "Nombre de la carpeta: ").grid(row = 1, column = 0)
		self.nombre_carpeta = Entry(frame_abrir)
		self.nombre_carpeta.focus()
		self.nombre_carpeta.grid(row = 1, column = 1)
		ttk.Button(frame_abrir, text = "Abrir Carpeta", command = self.abrir_carpeta).grid(row = 1, column = 3)

	#Esta funcion busca esa carpeta, y si la encuentra muestra el contenido de la misma
	def abrir_carpeta(self):
		delay = time.sleep(1)
		#if os.path.exists(self.nombre_carpeta_abrir.get()) == True:
		os.system("REN " +  self.nombre_carpeta.get() + ".{2559a1f2-21d7-11d4-bdaf-00c04f60b9f0}" + " " + self.nombre_carpeta.get())
		delay
		wb.open_new(self.nombre_carpeta.get())
		try:
			self.abrir.destroy()
			
		except AttributeError:
			pass

		




if __name__ == "__main__":

	root = Tk()
	aplicacion = SecureFolder(root)
	root.mainloop()

