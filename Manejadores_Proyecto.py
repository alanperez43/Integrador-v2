import csv
from Clase_Proyecto import Proyecto
class Manejador_Proyecto ():
    __lista_proyecto = None

    def __init__ (self):
        self.__lista_proyecto = []
    
    def Cargar_Archivo(self,archivo):
        archivo_proyecto = open(archivo)
        leer_archivo = csv.reader(archivo_proyecto,delimiter=";")
        bandera = 1
        for fila in leer_archivo:
            if bandera == 1:
                bandera = 0
            else:
                self.__lista_proyecto.append(Proyecto(fila[0],fila[1],fila[2]))
        archivo_proyecto.close()
    def mostrarProyectos(self):
        for li in self.__lista_proyecto:
            print(li)
    def Calcular_Puntos(self,manejador_integrante):
    
        for proyecto in self.__lista_proyecto:
            puntaje_de_cada_proyecto = manejador_integrante.Calcular_Puntos_integrantes(proyecto)
            
            proyecto.modifica(puntaje_de_cada_proyecto)
    def ordenar(self):
        self.__lista_proyecto.sort()        