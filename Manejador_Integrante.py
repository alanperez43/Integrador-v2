import csv 
from Clase_Integrante_Proyecto import Integrantes_Proyecto
class Manejador_Integrante ():
    __Lista_integrante = None

    def __init__ (self):
        self.__Lista_integrante = []
    
    def Cargar_Archivo_Integrante (self,archivo):
        archivo_integrantes = open(archivo)
        leer_archivo = csv.reader(archivo_integrantes,delimiter=";")
        bandera = 0
        for fila in leer_archivo:
            if bandera == 0:
                bandera=1
            else:
                self.__Lista_integrante.append(Integrantes_Proyecto(fila[0],fila[1],fila[2],fila[3],fila[4]))
        archivo_integrantes.close()
    
    def Calcular_Puntos_integrantes (self,idProyecto):
        acum_minimo = 0
        cont_director=0
        puntaje_proyecto = 0
        cont_codirector = 0
        #print(idProyecto)
        for integrante in self.__Lista_integrante:
            if integrante.getIdProyecto() == idProyecto.getIdProyecto():
                acum_minimo += 1
                if integrante.getRol().lower() == "director":
                    if integrante.getCategoria() == "I" or integrante.getCategoria() == "II":
                        cont_director += 1
                if integrante.getRol().lower() == "codirector":
                    if integrante.getCategoria() == "I" or integrante.getCategoria() == "II" or integrante.getCategoria() == "III":
                        cont_codirector += 1
    
        if acum_minimo > 2:
            puntaje_proyecto += 10
        else:
            puntaje_proyecto -= 20
            print("El proyecto {} debe tener como minimo 3 integrantes".format(idProyecto.getIdProyecto())) 
        
        if cont_director == 1:
            puntaje_proyecto += 10
        else: 
            print("El director del proyecto {} debe tener I o II".format(idProyecto.getIdProyecto()))
            puntaje_proyecto -= 5
        
        if cont_codirector == 1:
            puntaje_proyecto += 10
        else:
            print("El codirector del proyecto {} debe tener como minimo categoria III".format(idProyecto.getIdProyecto()))
            puntaje_proyecto -= 5

        if cont_director == 0 and cont_codirector == 0:
            puntaje_proyecto -=10

        return int(puntaje_proyecto)