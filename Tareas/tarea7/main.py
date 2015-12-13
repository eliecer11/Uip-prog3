import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import os.path

lista_asistencia=[]
class Asistencias(BoxLayout):
	def guardar(self,nombre):
		lista_asistencia.append(nombre)
		print (lista_asistencia)
	def exportar(self):	
		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		db_path = os.path.join(BASE_DIR, "Asistencias.txt")	
		archi=open(db_path,'a')
		for x in lista_asistencia:
			archi.write(x+" ")
			archi.write("\n")
		archi.close()
class RegistrosAPP(App):	
	def build(self):
		registro = Asistencias()
		return registro

if __name__ == "__main__":
    RegistrosAPP().run()
