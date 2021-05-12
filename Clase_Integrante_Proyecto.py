class Integrantes_Proyecto ():
    __IdProyecto = None
    __Apellido_y_Nombre = None
    __Dni = None
    __Categoria_investigador = None
    __rol = None

    def __init__ (self,IdP,AyN,dni,categoria,rol):
        self.__IdProyecto = IdP
        self.__Apellido_y_Nombre = AyN
        self.__Dni = dni
        self.__Categoria_investigador = categoria
        self.__rol = rol
    
    def getIdProyecto (self):
        return self.__IdProyecto

    def getRol (self):
        return self.__rol
    
    def getCategoria (self):
        return self.__Categoria_investigador
    