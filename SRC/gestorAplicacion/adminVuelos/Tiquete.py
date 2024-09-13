#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez, Jose Forero
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Pasajero import Pasajero
from gestorAplicacion.adminVuelos.Vuelo import Vuelo
from gestorAplicacion.hangar.Silla import Silla

#CLASE TIQUETE CONTIENE LA INFORMACION ASOCIADA AL VUELO, SILLA Y ALOJAMIENTOS SELECCIONADOS
#TAMBIEN CONTIENE UN ID PARA TIQUETE Y EL VALOR DEL PRECIO.
#SUS METODOS NOS PERMITEN CONSOLIDAR EL RESUMEN DEL TIQUETE QUE TIENE UN PASAJERO ASOCIADO A UN VUELO
class Tiquete:

    #ATRIBUTOS
    def __init__(self, id, precio, vuelo):
        self._id = id
        self._precio = precio
        self._vuelo = vuelo
        vuelo.get_tiquetes().append(self)

    def __init__(self, id, precio, vuelo, silla, pasajero, alojamiento):
        self._id = id
        self._precio = precio
        self._vuelo = vuelo
        self._silla = silla
        self._pasajero = pasajero
        self._alojamiento = alojamiento
        vuelo.get_tiquetes().append(self)

    #METODOS

    #ESTE METODO NO TIENE PARAMETROS DE ENTRADA PERO RETORNA UN BOOLEANO, YA QUE 
	#SU OBJETIVO ES ASIGNARLE EL PRECIO A CADA INSTANCIA DE TIQUETE OBTENIENDO LOS PRECIOS
	#DEL VUELO Y SILLA SELECCIONADOS CON UN DESCUENTO POR CONFORME AL ATRIBUTO EDAD DEL PASAJERO
    def asignar_precio():
        precio_total = _vuelo.get_precio() + self.get_silla().getClase().get_precio()
        if (pasajero.get_edad()<5):
            hayDescuento = True
            self._precio = (precio_total - (precio_total*0.25))

        elif(pasajero.get_edad()>5 and pasajero.get_edad()<=10):
            self._precio = (precio_total - (precio_total*0.15))
            hayDescuento = True
        else:
            self._precio = precio_total
        return hayDescuento
    
    #ESTE METODO SOBRECARGA EL METODO ASIGNAR PRECIO RECIBIENDO COMO PARAMETRO DE ENTRADA
	#UN ENTERO Y SU RETORNO ES VACIO. SU FUNCION SUMARLE A CADA INSTANCIA DE TIQUETE EL PRECIO DEL ALOJAMIENTO
	#SELECCIONADO DE ACUERDO AL NUMERO DE DIAS INGRESADO JUNTO A LOS PRECIOS DEL VUELO Y SILLA
    def asignar_precio(num_dias):
        precio_total = Vuelo.get_precio() + Alojamiento.calcular_precio(num_dias) + self.get_silla().getClase().get_precio()
        if (pasajero.get_edad() < 5):
            self._precio = (precio_total - (precio_total*0.15))
        elif (_pasajero.get_edad()>5 and _pasajero.get_edad()<=10):
            self._precio = (precio_total - (precio_total*0.15))
        else:
            self._precio = precio_total

    #EL METODO AGREGAR LA INSTANCIA DE TIQUETE CREADA AL ARRAY
    #DE TIQUETES QUE TIENE ASOCIADO AL VUELO SELCCIONADO, POR TAL RAZON NO RECIBE PARAMETRO Y SU
	#RETORNO ES VACIO
    def confirmar_compra():
        self._vuelo.get_tiquetes().append(self)

    #Espacio para devolver a la interfaz el recibo 



    #SETTER Y GETTER
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_precio(self, precio):
        self._precio = precio
    
    def get_precio(self):
        return self._precio

    def set_vuelo(self, vuelo):
        self._vuelo = vuelo

    def get_vuelo(self):
        return self._vuelo 
    
    def set_silla(self, silla):
        self._silla = silla
        silla.setEstado(False)
    
    def get_silla(self):
        return self._silla
    
    def set_pasajero(self, pasajero):
        self._pasajero = pasajero

    def get_pasajero(self):
        return self._pasajero

    def set_alojamiento(self, alojamiento):
        self._alojamiento = alojamiento
    
    def get_alojamiento(self):
        return self._alojamiento

    
