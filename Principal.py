from Manejador_Integrante import Manejador_Integrante
from Manejadores_Proyecto import Manejador_Proyecto
if __name__ == "__main__":
    ManejProyecto = Manejador_Proyecto()
    ManejIntegrante = Manejador_Integrante()
    ManejProyecto.Cargar_Archivo("proyectos.csv")
    ManejIntegrante.Cargar_Archivo_Integrante("integrantesProyecto.csv")
    ManejProyecto.Calcular_Puntos(ManejIntegrante)
    ManejProyecto.ordenar()
    ManejProyecto.mostrarProyectos()

    