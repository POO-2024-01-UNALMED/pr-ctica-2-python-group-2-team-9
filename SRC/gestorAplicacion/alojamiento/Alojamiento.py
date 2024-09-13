class Alojamiento():
    #ATRIBUTOS
    alojamientos = []
    
    def __init__(self, nombre, locacion, precioDia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precioDia = precioDia
        self._estrellas = estrellas

    def calcularPrecio(self, dias):
        return dias * (self._precioDia)
