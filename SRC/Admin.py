#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez, Jose Forero
#CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA

import random
import pickle

class Admin(object):

    # MUESTRA UNA TABLA POR CADA AEROLINEA CON LOS VUELOS QUE SE TIENEN DISPONIBLES
    @staticmethod
    def mostrarVuelosPorAerolineas(frame_operaciones):
        aerolineasDisponibles = Aerolinea.getAerolineas()
        return Admin.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles,frame_operaciones)