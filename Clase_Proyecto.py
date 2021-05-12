class Proyecto ():
    __IdProyecto = None
    __Titulo = None
    __Palabra_Clave = None
    __Puntaje=None

    def __init__ (self,IdP,titulo,palabra):
        self.__IdProyecto = IdP
        self.__Titulo = titulo
        self.__Palabra_Clave = palabra
        self.__Puntaje=0
    
    def getIdProyecto (self):
        return self.__IdProyecto
    def getTitulo(self):
        return self.__Titulo
    def getPalabras(self):
        return self.__Palabra_Clave
    def modifica(self,punto):
        self.__Puntaje=punto
    def getPuntaje(self):
        return int(self.__Puntaje)
    def __gt__(self, otroProyecto):
        '''utilizado para ordenar de mayor a menor los Proyectos, según el puntaje obtenido'''
        return self.getPuntaje() < otroProyecto.getPuntaje()
    def __str__(self):
        '''devuelve una cadena con los datos del Proyecto y de los integrantes del mismo'''
        s = "\nPuntaje del Proyecto: {} ".format(self.getPuntaje())
        s += "\nId del Proyecto: {} " .format(self.__IdProyecto)
        s += "\nTitulo: {}" .format(self.__Titulo)  
        s += "\nPalabras Clave: {}" .format(self.__Palabra_Clave)
       
        
        return s