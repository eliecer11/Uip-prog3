from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition

# IMPORTANDO MODULOS 
from configurador import Guardar_datos
class Principal(ScreenManager):
	#Acceder a los  atributos del Textinput
	nombre=ObjectProperty()
	cedula=ObjectProperty()
	correo=ObjectProperty()
	modelo=ObjectProperty()
	serie=ObjectProperty()
	otros=ObjectProperty()

	datos_completos=[]
	def cliente(self):
		#Obtencion de los datos Escritos por el Usuario
		nombre=self.nombre.text
		cedula=self.cedula.text
		correo=self.correo.text

		#Agregamos los datos a la lista que se exportara
		self.datos_completos.append(nombre)
		self.datos_completos.append(cedula)
		self.datos_completos.append(correo)
	def computadora(self):
		#Obtencion de los datos Escritos por el Usuario
		modelo=self.modelo.text
		serie=self.serie.text
		otros=self.otros.text

		#Agregamos los datos a la lista que se exportara
		self.datos_completos.append(modelo)
		self.datos_completos.append(serie)
		self.datos_completos.append(otros)
	def eliminar(self):
		#Asignamos todos los campos en vacios
		self.nombre.text=""
		self.cedula.text=""
		self.correo.text=""
		self.modelo.text=""
		self.serie.text=""
		self.otros.text=""
		self.datos_completos=[]	

	def guardar(self):
		#Verificamos que no allan dejado campos vacios
		if "" in self.datos_completos:
			print ("El Sistema no Guarda datos Incompleto")
		else:
		# llamamos a la funcion guardar datos que ara el proceso de exportacion
			Guardar_datos(self.datos_completos)
			self.eliminar()
		#reasignamos la lista para que quede vacia
		self.datos_completos=[]	

class AplicacionApp(App):
	def build(self):
		principal  = Principal()
		return principal
		
if __name__ == "__main__":
	AplicacionApp().run()