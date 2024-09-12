class Alojamiento():
    #ATRIBUTOS
    def __init__(self, nombre, locacion, precioDia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precioDia = precioDia
        self._estrellas = estrellas
        #De clase 
        self._alojamientos = []

    def calcularPrecio(self, dias):
        return dias * (self._precioDia)
