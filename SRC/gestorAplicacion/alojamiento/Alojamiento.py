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
    def calcular_precio(self, dias):
        return dias * (self._precioDia)

#BUSCAR ALOJAMIENTOS POR ...

    #METODO DE CLASE QUE RECIBE UNA UBICACION(String) Y BUSCA ENTRE LOS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO EN ESTA LOCACION, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @classmethod
    def buscar_alojamiento_por_ubicación(cls, ubicacion):
      alojamientosEnUbicacion = []
      for i in range(len(cls.alojamientos)):
        if cls.alojamientos[i].get_locacion().lower() == ubicacion.lower():
          alojamientosEnUbicacion.append(cls.alojamientos[i])

      return alojamientosEnUbicacion

    #METODO DE CLASE QUE RECIBE UNA NOMBRE(String) Y BUSCA ENTRE LAS ALOJAMIENTOS DISPONIBLES SI HAY ALGUNO CON ESTE NOMBRE, 
    #SI ES ASI, RETORNA ESE OBJETO ALOJAMIENTO, SI NO, DEVUELVE NULL.
    @classmethod
    def buscar_alojamiento_por_nombre(cls, nombre):
        for i in range(len(cls.alojamientos)):
          if cls.alojamientos[i].get_nombre().lower() == nombre.lower():
            return cls.alojamientos[i]
         
        return None
    
    #SETTER Y GETTER
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_nombre(self):
        return self._nombre

    def set_locacion(self, locacion):
        self._locacion = locacion

    def get_locacion(self):
        return self._locacion

    def set_precio_dias(self, precio_dias):
        self._precioDia = precio_dias

    def get_precio_dia(self):
        return self._precioDia

    def set_alojamientos(self, alojamientos):
        Alojamiento.alojamientos = alojamientos

    def get_alojamientos(self):
        return self.alojamientos

    def set_estrellas(self, estrellas):
        self._estrellas = estrellas

    def get_estrellas(self):
        return self._estrellas