#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez
#CLASE ALOJAMIENTO POSEE LA INFORMACION DE TODOS LOS ALOJAMIENTOS CREADOS, CON LOS ATRIBUTOS NOMBRE, LOCACION, PRECIO POR DIA Y
#NUMERO DE ESTRELLAS.
class Alojamiento():
    #ATRIBUTOS
    _alojamientos = []

    #CONSTRUCTORES
    def __init__(self, nombre, locacion, precio_dia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precio_dia = precio_dia
        self._estrellas = estrellas
        Alojamiento._alojamientos.append(self)

    #EL METODO RECIBE UN PARAMETRO DIAS (int) Y RETORNA EL PRECIO RESULTANTE AL MULTIPLICAR EL PRECIO POR DIA DEL ALOJAMIENTO
    #CON EL PARAMETRO DIAS QUE SE LE PASO.
    def calcularPrecio(self, dias):
        return int((dias * self._precioDia))

#BUSCAR ALOJAMIENTOS POR ...

    #METODO DE CLASE QUE RECIBE UNA UBICACION(String) Y BUSCA ENTRE LOS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO EN ESTA LOCACION, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @classmethod
    def buscarAlojamientoPorUbicacion(cls, ubicacion):
        alojamientosEnUbicacion = []
        i = 0
        while i < len(Alojamiento._alojamientos):
            if Alojamiento._alojamientos[i].getLocacion().casefold() == ubicacion.casefold():
                alojamientosEnUbicacion.append(Alojamiento._alojamientos[i])
            i += 1
        return alojamientosEnUbicacion

    #METODO DE CLASE QUE RECIBE UNA NOMBRE(String) Y BUSCA ENTRE LAS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO CON ESTE NOMBRE, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @staticmethod
    def buscarAlojamientoPorNombre(nombre):
        i = 0
        while i < len(Alojamiento._alojamientos):
            if Alojamiento._alojamientos[i].getNombre().casefold() == nombre.casefold():
                return Alojamiento._alojamientos[i]
            i += 1
        return None
    
    #SETTER Y GETTER
    def setLocacion(self, locacion):
        self._locacion = locacion

    def setPrecio_dias(self, precio_dias):
        self._precio_dia = precio_dias

    @staticmethod
    def getAlojamientos():
        return Alojamiento._alojamientos

    @staticmethod
    def setAlojamientos(alojamientos):
        Alojamiento._alojamientos = alojamientos

    def getPrecio_dia(self):
        return self._precio_dia

    def setPrecio_dia(self, precio_dia):
        self._precio_dia = precio_dia

    def getLocacion(self):
        return self._locacion

    def getEstrellas(self):
        return self._estrellas

    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre