# AUTORES: RICARDO FUENTES, VALERY FERNANDEZ, JUAN LUIS SUCERQUIA, MARIANA SANCHEZ
from tkinter import messagebox
from tkinter.ttk import Combobox
from excepciones.ErrorAplicacion import *
from excepciones.ErrorAsignacion import *
from excepciones.ErrorFormato  import *
from tkinter import *
from FieldFrame import *
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Aerolinea import Aerolinea

class VentanaSecundaria(Toplevel):
    en_uso = False #Permite saber si hay una ventanaSecundaria abierta
