#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez, Jose Forero
#CLASE ALOJAMIENTO POSEE LA INFORMACION DE TODOS LOS ALOJAMIENTOS CREADOS, CON LOS ATRIBUTOS NOMBRE, LOCACION, PRECIO POR DIA Y
#NUMERO DE ESTRELLAS.
class Alojamiento():
    #ATRIBUTOS
    alojamientos = []

    def __init__(self, nombre, locacion, precioDia, estrellas):
        self._nombre = nombre
        self._locacion = locacion
        self._precioDia = precioDia
        self._estrellas = estrellas
        self.alojamientos.append(self)

    #EL METODO RECIBE UN PARAMETRO DIAS (int) Y RETORNA EL PRECIO RESULTANTE AL MULTIPLICAR EL PRECIO POR DIA DEL ALOJAMIENTO
    #CON EL PARAMETRO DIAS QUE SE LE PASO.
    def calcularPrecio(self, dias):
        return dias * (self._precioDia)

#BUSCAR ALOJAMIENTOS POR ...

    #METODO DE CLASE QUE RECIBE UNA UBICACION(String) Y BUSCA ENTRE LOS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO EN ESTA LOCACION, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @classmethod
    def buscarAlojamientoPorUbicación(cls, ubicacion):
        alojamientosEnUbicacion = []
        for i in range(len(alojamientos)):

            if alojamientos[i].getLocacion().lower() == ubicacion.lower():
                alojamientosEnUbicacion.append(alojamientos.get(i))

        return alojamientosEnUbicacion

    #METODO DE CLASE QUE RECIBE UNA NOMBRE(String) Y BUSCA ENTRE LAS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO CON ESTE NOMBRE, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @classmethod
    def buscarAlojamientoPorNombre(cls, nombre):
        for i in range(len(alojamientos)):

            if alojamientos[i].getNombre().lower() == nombre.lower():
                return alojamientos[i]
        
        return null
    
    #SETTER Y GETTER
    def setLocacion(self, locacion):
        self._locacion = locacion

    def getLocacion(self):
        return self._locacion

    def setPrecio_dias(self, precio_dias):
        self._precioDia = precio_dias

    def getPrecio_dia(self):
        return self._precioDia

    def setAlojamientos(self, alojamientos):
        Alojamiento.alojamientos = alojamientos

    def getAlojamientos(self):
        return self.alojamientos

    def setEstrellas(self, estrellas):
        self._estrellas = estrellas

    def getEstrellas(self):
        return self._estrellas