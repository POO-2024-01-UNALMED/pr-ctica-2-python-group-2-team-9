#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez, Jose Forero
#CLASE ADMIN PARA LA INTERACCION DEL USUARIO CON EL SISTEMA
import random
import pickle
from tkinter import *

from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Vuelo import Vuelo
from gestorAplicacion.hangar.Avioneta import Avioneta

class Admin(object):

    @staticmethod
    def mostrarVuelosPorAerolineas(frame_operaciones):
        aerolineasDisponibles = Aerolinea.getAerolineas()
        return Admin.mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineasDisponibles,frame_operaciones)
    
    @staticmethod
    def obtenerAlojamientos():
        lista_alojamientos= Alojamiento.getAlojamientos()
        valores =[]
        for alojamiento in lista_alojamientos:
            valores.append(alojamiento.getNombre()+"---"+alojamiento.getLocacion())
        return valores

    @staticmethod
    def asignarTiquete(datos,tiquete):
        nombre = datos[0]
        edad = int(datos[1])
        pasaporte = datos[2]
        correo = datos[-1]
        pasajero = Pasajero(pasaporte, nombre, tiquete, edad, correo)
        tiquete.setPasajero(pasajero)
    
    @staticmethod
    def solicitarAlojamiento(tiquete_solicitado,alojamiento_nombre):
        destino = tiquete_solicitado.getVuelo().getDestino()
        alojamiento_solicitado = Alojamiento.buscarAlojamientoPorNombre(alojamiento_nombre)
        if alojamiento_solicitado == None:
            return alojamiento_solicitado 
        elif  alojamiento_solicitado.getLocacion().lower() != destino.lower():
            alojamiento_solicitado = None 
            return alojamiento_solicitado
        else:
            return alojamiento_solicitado 

    @staticmethod
    def agregarAlojamiento(tiquete_solicitado,alojamiento_solicitado,num_dias):
        tiquete_solicitado.setAlojamiento(alojamiento_solicitado)
        tiquete_solicitado.asignarPrecio(int(num_dias))


    @staticmethod
    def modificarSilla(numero, tiquete,silla):
        if numero ==1 :
            tiquete.setSilla(silla)
        else:    
            tiquete.getSilla().setEstado(True) 
            tiquete.setSilla(silla)
        tiquete.asignarPrecio() 
    
    @staticmethod
    def agregarNuevoVuelo(valores):
        nombreAerolinea = valores[0]
        iD = int(valores[1])
        precio= int(valores[2])
        origen = valores[3]
        destino = valores[4]
        distancia = int(valores[5])
        fechaSalida=valores[6]
        horaSalida = valores[7]
        aeronave = valores[8]
        nombreAeronave = valores[9]
        for aerolinea in Aerolinea.getAerolineas():
            existe_vuelo= aerolinea.buscarVueloPorID(aerolinea.getVuelos(),iD)
            if existe_vuelo !=None:
                return True

        if aeronave.lower() == "avion":
            avion = Avion(nombreAeronave, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avion, distancia, fechaSalida, horaSalida)
    
        elif aeronave.lower() == "avioneta":
            avioneta = Avioneta(nombreAeronave, Aerolinea.buscarAerolineaPorNombre(nombreAerolinea))
            vuelo = Vuelo(iD, precio, origen, destino, avioneta, distancia, fechaSalida, horaSalida)
        return False  


    @staticmethod
    def cancelarVuelos(id):
        vuelo_encontrado = False
        aerolineas = Aerolinea.getAerolineas()
        id = id
        for aerolinea in aerolineas:
            i = 0
            while i < len(aerolinea.getVuelos()):
                if aerolinea.buscarVueloPorID(aerolinea.getVuelos(), id) != None:
                    aerolinea.cancelarVuelo(id)
                    vuelo_encontrado = True
                    break 
                i += 1
        return vuelo_encontrado


    @staticmethod
    def retirarAvion(aeronave):
        aeronave_encontrada = False
        nombre_aeronave = aeronave
        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            
            vuelo = aerolinea.buscarVueloPorAeronave(aerolinea.getVuelos(), nombre_aeronave)
            if vuelo != None:
                vuelo.getAeronave().setDescompuesto(True)
                aerolinea.cancelarVuelo(vuelo.getID())
                aeronave_encontrada = True
                break
            i += 1
        
        return aeronave_encontrada

    @staticmethod
    def nuevoAlojamiento(valores):

        nombre = valores[0]
        locacion = valores[1]
        precio = valores[2]
        estrellas = valores[3]

        nuevoAlojamiento = Alojamiento(nombre, locacion, precio, estrellas)

    @staticmethod
    def retirarAlojamiento(nombre):
        alojamiento_encontrado = False
        if Alojamiento.buscarAlojamientoPorNombre(nombre) != None:
            i = 0
            while i < len(Alojamiento.getAlojamientos()):
                if Alojamiento.getAlojamientos()[i].getNombre().lower() == nombre.lower():
                    Alojamiento.getAlojamientos().pop(i)
                    alojamiento_encontrado = True
                    break
                i += 1
        return alojamiento_encontrado

    @staticmethod
    def salirDelSistema():
        picklefile = open('SRC/baseDatos/Aerolineas', 'wb')
        picklefile2 = open('SRC/baseDatos/Alojamientos','wb')
        pickle.dump(Aerolinea._aerolineas, picklefile)
        pickle.dump(Alojamiento._alojamientos,picklefile2)
        picklefile.close()
        picklefile2.close()
        quit()
    
    @staticmethod
    def consultarVuelosPorDestino(destino, frame_operaciones):
        lista_vuelos_nombres = []
        vuelos = []
        nombreAerolineas =[]

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                label = Label(frame_operaciones)
                Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorDestino, label)
                vuelos.append(label)
                nombreAerolineas.append(aerolinea.getNombre())
            i += 1

        lista_vuelos_nombres.append(vuelos)
        lista_vuelos_nombres.append(nombreAerolineas)

        return lista_vuelos_nombres

    @staticmethod
    def consultarVuelosPorDestinoYFecha(destino, fecha, frame_operaciones):

        lista_vuelos_nombres = []
        vuelos = []
        nombreAerolineas =[]

        aerolineasDisponibles = Aerolinea.getAerolineas()
        i = 0
        while i < len(aerolineasDisponibles):
            aerolinea = aerolineasDisponibles[i]
            vuelosPorDestino = aerolinea.buscarVueloPorDestino(aerolinea.vuelosDisponibles(aerolinea.getVuelos()), destino)
            if len(vuelosPorDestino) != 0:
                vuelosPorFecha = aerolinea.buscarVueloPorFecha(vuelosPorDestino, fecha)
                if len(vuelosPorFecha) != 0:
                    label = Label(frame_operaciones)
                    Admin.mostrarTablaDeVuelos(aerolinea, vuelosPorFecha, label)
                    vuelos.append(label)
                    nombreAerolineas.append(aerolinea.getNombre())
            i += 1
        
        lista_vuelos_nombres.append(vuelos)
        lista_vuelos_nombres.append(nombreAerolineas)

        return lista_vuelos_nombres

    @staticmethod
    def elegirSilla(tiquete,datos_silla):
        clase =str( datos_silla[0])
        ubicacion = str(datos_silla[1])

        if ubicacion.lower() == "pasillo":
            ubicacion = Ubicacion.PASILLO
        elif ubicacion.lower() == "ventana":
            ubicacion = Ubicacion.VENTANA
        else:
            ubicacion = Ubicacion.CENTRAL

        return tiquete.getVuelo().getAeronave().buscarSillaPorUbicacionyTipo(ubicacion,clase)

    @staticmethod
    def mostrarTablaDePasajeros(tiquetes,label):
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>12} {2:>16} {3:>17}".format("ID", "NOMBRE", "PASAPORTE", "EMAIL"+"\n")
        label["text"]+="---------------------------------------------------------------"

        i = 0
        while i < len(tiquetes):
            label["text"]+="\n"+"{0:>5} {1:>13} {2:>12} {3:>26}".format(str(tiquetes[i].getId()), tiquetes[i].getPasajero().nombre, tiquetes[i].getPasajero().getPasaporte(), tiquetes[i].getPasajero().getEmail())
            i += 1
        label["text"]+="\n---------------------------------------------------------------"
        label["text"]+="\n"

    @staticmethod
    def mostrarTablaDeAlojamientos(alojamientos, label):
        label["text"]+="\n"
        label["text"]+="\n"+ "-------------------------------------------------------------"
        label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
        label["text"]+="\n"
        label["text"]+="\n"+"-------------------------------------------------------------"

        j = 0
        while j < len(alojamientos):
            label["text"]+="\n"+"{0:>13} {1:>11} {2:>16} {3:>11}".format(alojamientos[j].getNombre(), alojamientos[j].getLocacion(), alojamientos[j].getPrecio_dia(), alojamientos[j].getEstrellas())
            label["text"]+="\n"
            j += 1

        label["text"]+="\n"+"-------------------------------------------------------------"
        label["text"]+="\n"

    @staticmethod
    def mostrarTablaDeVuelosDisponiblesPorAerolineas(aerolineas,frame_operaciones):
        i = 0
        lista = []
        while i < len(aerolineas):
            label = Label(frame_operaciones)
            aerolinea = aerolineas[i]
            Admin.printEncabezadoAerolinea(aerolineas[i],label)
            Admin.printVuelos(aerolinea.vuelosDisponibles(aerolinea.getVuelos()),label)
            Admin.printSeparador(label)
            lista.append(label)
            i += 1
        return lista

    @staticmethod
    def mostrarTablaDeVuelos(aerolinea,vuelos,label):
        if len(vuelos) != 0:
            Admin.printEncabezadoAerolinea(aerolinea,label)
            Admin.printVuelos(vuelos,label)
            Admin.printSeparador(label)
        return label

    @staticmethod
    def printEncabezadoAerolinea(aerolinea,label):
        label["text"]+="\n"+"VUELOS DISPONIBLES DE LA AEROLINEA " + aerolinea.getNombre().upper()
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>4} {1:>13} {2:>12} {3:>14} {4:>12} {5:>22} {6:>12}".format("ID", "PRECIO", "ORIGEN", "DESTINO", "FECHA", "HORA DE SALIDA", "AERONAVE")
        label["text"]+="\n"
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
    
    @staticmethod
    def printVuelos(vuelos,label):
        j = 0
        while j < len(vuelos):
            label["text"]+="\n"+"{0:>5} {1:>12} {2:>13} {3:>13} {4:>15} {5:>11} {6:>21}".format(vuelos[j].getID(), vuelos[j].getPrecio(), vuelos[j].getOrigen(), vuelos[j].getDestino(), vuelos[j].getFecha_de_salida(), vuelos[j].getHora_de_salida(), vuelos[j].getAeronave().getNombre())
            label["text"]+="\n"
            j += 1

    @staticmethod
    def printSeparador(label):
        label["text"]+="\n"+"--------------------------------------------------------------------------------------------------"
        label["text"]+="\n"