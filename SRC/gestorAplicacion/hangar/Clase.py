#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez

from enum import Enum

class Clase(Enum):
    ECONOMICA = 10000
    EJECUTIVA = 70000

    def setPrecio(self, precio): 
       self._precio = precio